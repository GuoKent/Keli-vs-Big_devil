class GameStats():
    """跟踪游戏统计信息"""
    def __init__(self,ai_setting):
        """初始化统计信息"""
        self.ai_settings=ai_setting
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active=False
        # 在如何情况下都不应重置最高得分
        self.high_score=0
    def reset_stats(self):
        """初始化在游戏运行期间可能发生的变化"""
        self.ship_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
