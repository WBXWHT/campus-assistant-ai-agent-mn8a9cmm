import json
import datetime
import random

class CampusAssistantAI:
    """校园助手AI Agent核心类"""
    
    def __init__(self):
        # 模拟用户数据库（实际项目中应使用真实数据库）
        self.user_profiles = {}
        # 模拟任务历史记录
        self.task_history = {}
        # 模拟大模型响应（实际应调用API）
        self.model_responses = {
            "学习": ["建议使用番茄工作法，专注学习45分钟后休息5分钟", 
                   "根据艾宾浩斯遗忘曲线，建议在1小时后复习一次"],
            "作业": ["优先完成截止日期最近的作业", 
                   "将大作业分解为多个小任务，每天完成一部分"],
            "考试": ["制定详细的复习计划，每天覆盖2-3个章节",
                   "建议制作思维导图帮助记忆"],
            "运动": ["每周至少进行3次有氧运动，每次30分钟",
                   "运动前做好热身，防止受伤"],
            "休息": ["保证每天7-8小时睡眠，避免熬夜",
                   "每小时起身活动5分钟，缓解久坐疲劳"]
        }
    
    def parse_user_input(self, user_input):
        """解析用户输入，识别任务类型（模拟大模型解析）"""
        # 实际项目中这里会调用大模型API进行智能解析
        # 这里使用关键词匹配进行模拟
        task_types = ["学习", "作业", "考试", "运动", "休息"]
        for task_type in task_types:
            if task_type in user_input:
                return task_type
        return "其他"
    
    def generate_recommendation(self, task_type, user_id):
        """生成个性化推荐（模拟大模型推荐）"""
        # 获取用户历史记录
        user_history = self.task_history.get(user_id, [])
        
        # 模拟A/B测试优化后的提示词效果
        # 基础推荐
        if task_type in self.model_responses:
            recommendations = self.model_responses[task_type]
            
            # 模拟优化后的准确率提升（92%准确率）
            if random.random() < 0.92:  # 92%准确率
                # 个性化调整：根据历史记录优化推荐
                if len(user_history) > 3:
                    recommendation = recommendations[1] + "（根据您的活跃历史优化）"
                else:
                    recommendation = recommendations[0] + "（基础推荐）"
            else:
                recommendation = "暂时无法提供具体建议，请尝试更详细的描述"
        else:
            recommendation = "已记录您的需求，稍后将为您规划"
        
        return recommendation
    
    def create_schedule(self, user_id, tasks):
        """创建日程规划"""
        schedule = []
        start_time = datetime.datetime.now().replace(hour=9, minute=0, second=0)
        
        for i, task in enumerate(tasks):
            task_time = start_time + datetime.timedelta(hours=i*2)
            schedule.append({
                "时间": task_time.strftime("%H:%M"),
                "任务": task["description"],
                "类型": task["type"],
                "推荐": task["recommendation"]
            })
        
        return schedule
    
    def process_user_request(self, user_id, user_input):
        """处理用户请求的主流程"""
        print(f"\n用户 {user_id} 的请求: {user_input}")
        
        # 1. 智能解析任务类型
        task_type = self.parse_user_input(user_input)
        print(f"识别到的任务类型: {task_type}")
        
        # 2. 生成个性化推荐
        recommendation = self.generate_recommendation(task_type, user_id)
        print(f"AI推荐: {recommendation}")
        
        # 3. 更新用户历史记录
        if user_id not in self.task_history:
            self.task_history[user_id] = []
        
        task_record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "input": user_input,
            "type": task_type,
            "recommendation": recommendation
        }
        self.task_history[user_id].append(task_record)
        
        # 4. 生成今日日程建议（如果有多个任务）
        if len(self.task_history[user_id]) >= 2:
            recent_tasks = self.task_history[user_id][-2:]
            schedule = self.create_schedule(user_id, recent_tasks)
            print("\n今日日程建议:")
            for item in schedule:
                print(f"  {item['时间']} - {item['任务'][:10]}... | {item['推荐'][:20]}...")
        
        # 5. 计算并返回活跃度
        weekly_activity = self.calculate_weekly_activity(user_id)
        print(f"本周活跃度: {weekly_activity}%")
        
        return {
            "task_type": task_type,
            "recommendation": recommendation,
            "weekly_activity": weekly_activity
        }
    
    def calculate_weekly_activity(self, user_id):
        """计算用户本周活跃度（模拟数据）"""
        # 模拟活跃度提升20%
        base_activity = 60  # 基础活跃度
        optimized_activity = 80  # 优化后活跃度
        
        # 根据用户历史记录长度决定活跃度
        user_history = self.task_history.get(user_id, [])
        if len(user_history) > 5:
            return optimized_activity
        return base_activity

def main():
    """主函数 - 程序入口"""
    print("=" * 50)
    print("校园助手AI Agent v1.0")
    print("=" * 50)
    
    # 初始化AI助手
    assistant = CampusAssistantAI()
    
    # 模拟用户交互
    test_cases = [
        {"user_id": "student_001", "input": "明天要考试了，怎么复习？"},
        {"user_id": "student_001", "input": "有大量作业需要完成"},
        {"user_id": "student_001", "input": "最近学习效率不高"},
        {"user_id": "student_002", "input": "需要制定运动计划"},
        {"user_id": "student_002", "input": "如何合理安排休息时间"}
    ]
    
    print("\n模拟用户请求处理:")
    print("-" * 50)
    
    # 处理所有测试用例
    results = []
    for test_case in test_cases:
        result = assistant.process_user_request(
            test_case["user_id"], 
            test_case["input"]
        )
        results.append(result)
        print("-" * 50)
    
    # 输出统计信息
    print("\n处理完成统计:")
    print(f"总处理请求数: {len(results)}")
    
    # 计算平均准确率（模拟）
    successful_tasks = sum(1 for r in results if r["task_type"] != "其他")
    accuracy = (successful_tasks / len(results)) * 100
    print(f"任务识别准确率: {accuracy:.1f}%")
    
    # 计算平均活跃度
    avg_activity = sum(r["weekly_activity"] for r in results) / len(results)
    print(f"平均用户活跃度: {avg_activity:.1f}%")
    
    print("\n项目特点演示:")
    print("1. 基于大模型的智能任务解析")
    print("2. 个性化学习推荐生成")
    print("3. A/B测试优化的提示词结构")
    print("4. 用户活跃度跟踪与提升")

if __name__ == "__main__":
    main()