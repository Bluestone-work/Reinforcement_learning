import time
from typing import Optional, Union, List, Tuple

import gym
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from gym import spaces
from gym.core import RenderFrame, ActType, ObsType
np.random.seed(1)
import render


def arr_in_list(array, _list):
    for element in _list:
        if np.array_equal(element, array):
            return True
    return False


class GridEnv(gym.Env):

    def __init__(self, size: int, target: Union[list, tuple, np.ndarray], forbidden: Union[list, tuple, np.ndarray],
                 render_mode: str):
        """
        GridEnv 的构造函数
        :param size: grid_world 的边长
        :param target: 目标点的pos
        :param forbidden: 不可通行区域 二维数组 或者嵌套列表 如 [[1,2],[2,2]]
        :param render_mode: 渲染模式 video表示保存视频
        """
        # 初始化可视化
        self.agent_location = np.array([0, 0])
        self.time_steps = 0
        self.size = size
        self.render_mode = render_mode
        self.render_ = render.Render(target=target, forbidden=forbidden, size=size)
        # 初始化起点 障碍物 目标点
        self.forbidden_location = []
        for fob in forbidden:
            self.forbidden_location.append(np.array(fob))
        self.target_location = np.array(target)
        # 初始化 动作空间 观测空间
        self.action_space, self.action_space_size = spaces.Discrete(5), spaces.Discrete(5).n
        self.reward_list = [0, 1, -0.1, -0.1]
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, size - 1, shape=(2,), dtype=int),
                "target": spaces.Box(0, size - 1, shape=(2,), dtype=int),
                "barrier": spaces.Box(0, size - 1, shape=(2,), dtype=int),
            }
        )
        # action to pos偏移量 的一个map
        self.action_to_direction = {
            0: np.array([-1, 0]),
            1: np.array([0, 1]),
            2: np.array([1, 0]),
            3: np.array([0, -1]),
            4: np.array([0, 0]),
        }
        # Rsa表示 在 指定 state 选取指点 action 得到reward的概率
        self.Rsa = None
        # Psa表示 在 指定 state 选取指点 action 跳到下一个state的概率
        self.Psa = None
        self.psa_rsa_init()

    def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None, ) -> Tuple[ObsType, dict]:
        super().reset(seed=seed)
        self.agent_location = np.array([0, 0])
        observation = self.get_obs()
        info = self.get_info()
        return observation, info

    def step(self, action: ActType) -> Tuple[ObsType, float, bool, bool, dict]:
        #self.agent_location 是智能体当前所在的位置。通过 self.pos2state(self.agent_location)，将该位置转换为一个对应的状态索引。
        #self.Rsa[self.pos2state(self.agent_location), action] 返回的是一个关于该状态和动作的奖励分布（例如，[0, 1, 0, 0]，其中某一类奖励是 1）。tolist() 将这个 NumPy 数组转换为 Python 列表。
        #然后，通过 .index(1) 找到奖励分布中值为 1 的奖励类别的索引，这个索引对应于 reward_list 中的某个奖励值。
        #最后，通过 self.reward_list[...] 获取该动作执行后的具体奖励值。
        reward = self.reward_list[self.Rsa[self.pos2state(self.agent_location), action].tolist().index(1)]
        #self.action_to_direction[action] 将动作 action 映射为一个方向向量。例如，假设 action 是“向上”或“向右”，那么 direction 就会是一个二维的移动向量，如 [0, 1]（表示向右移动一个单位）。
        direction = self.action_to_direction[action]
        self.render_.upgrade_agent(self.agent_location, direction, self.agent_location + direction)
        #self.agent_location + direction 计算智能体在执行动作后的新位置。
        #np.clip(...) 将智能体的新位置限制在网格世界的范围内，确保位置不会超出网格的边界（例如，如果网格大小是 size x size，那么位置必须在 [0, size-1] 之间）。
        self.agent_location = np.clip(self.agent_location + direction, 0, self.size - 1)
        #这里使用 np.array_equal 判断当前的智能体位置是否等于目标位置。如果智能体已经到达目标位置，terminated 会被设置为 True，表示该回合结束。
        terminated = np.array_equal(self.agent_location, self.target_location)
        observation = self.get_obs()
        info = self.get_info()
        return observation, reward, terminated, False, info

    def render(self) -> Optional[Union[RenderFrame, List[RenderFrame]]]:
        if self.render_mode == "video":
            self.render_.save_video('image/' + str(time.time()))
        self.render_.show_frame(0.3)
        return None

    def get_obs(self) -> ObsType:
        return {"agent": self.agent_location, "target": self.target_location, "barrier": self.forbidden_location}

    def get_info(self) -> dict:
        return {"time_steps": self.time_steps}

    def state2pos(self, state: int) -> np.ndarray:
        return np.array((state // self.size, state % self.size))

    def pos2state(self, pos: np.ndarray) -> int:
        return pos[0] * self.size + pos[1]

    def psa_rsa_init(self):
        state_size = self.size ** 2
        self.Psa = np.zeros(shape=(state_size, self.action_space_size, state_size), dtype=float)#Psa[s, a, s'] 表示在状态 s 下执行动作 a 后，转移到状态 s' 的概率。
        self.Rsa = np.zeros(shape=(self.size ** 2, self.action_space_size, len(self.reward_list)), dtype=float)#Rsa[s, a, r] 表示在状态 s 下执行动作 a 后，获得的第 r 类奖励的数值。
        for state_index in range(state_size):#这里遍历所有的状态 state_index 以及每个状态下所有可能的动作 action_index，分别为每个状态和动作设置相应的转移概率和奖励。
            for action_index in range(self.action_space_size):
                pos = self.state2pos(state_index)#pos 是当前状态 state_index 对应的网格位置。
                next_pos = pos + self.action_to_direction[action_index]#next_pos 是根据当前动作 action_index 计算出的下一个位置。
                if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] > self.size - 1 or next_pos[1] > self.size - 1:#如果越界，则设置 Psa[state_index, action_index, state_index] = 1，表示在该动作下，智能体会停留在原状态 state_index，而不会转移到其他状态。
                    self.Psa[state_index, action_index, state_index] = 1
                    self.Rsa[state_index, action_index, 3] = 1#同时，将 Rsa[state_index, action_index, 3] = 1，表示此时智能体执行该动作会获得一个负向奖励（对应 reward_list[3] = -10，代表撞墙或无效动作）。

                else:#更新 Psa，即从状态 state_index 执行动作 action_index 后，转移到状态 next_pos 对应的状态。
                    self.Psa[state_index, action_index, self.pos2state(next_pos)] = 1
                    if np.array_equal(next_pos, self.target_location):#如果 next_pos 是目标位置，则更新 Rsa，给与正向奖励（对应 reward_list[1] = 1），表示智能体成功到达目标。
                        self.Rsa[state_index, action_index, 1] = 1
                    elif arr_in_list(next_pos, self.forbidden_location):#如果 next_pos 是禁区或不允许进入的区域，则更新 Rsa，给与负向奖励（对应 reward_list[2] = -10），表示智能体进入了一个危险区域。
                        self.Rsa[state_index, action_index, 2] = 1
                    else:#如果 next_pos 既不是目标位置，也不是禁区，则给与中性奖励（对应 reward_list[0] = 0），表示普通的状态转移，没有特殊的奖励或惩罚。
                        self.Rsa[state_index, action_index, 0] = 1

    def close(self):
        pass

if __name__ == "__main__":
    grid = GridEnv(size=5, target=[1, 2], forbidden=[[2, 2]], render_mode='')
    grid.render()