class BlackSwan:
    """
    在经济学中，所谓的“黑天鹅”（Black Swan）指的是一种罕见且极端事件，其特征包括：
    非常罕见：“黑天鹅”事件是一种极其罕见的事件，远远超出了正态分布的范畴。它们往往是在我们的预期之外，几乎无法预测或预见的。
    对经济系统具有巨大的影响：虽然罕见，但“黑天鹅”事件可能对整个经济系统产生深远的影响，引发大规模的不确定性和动荡，对市场和经济产生严重的冲击。
    事后容易被解释：虽然“黑天鹅”事件在发生之前难以预见，但在事件发生后，人们往往会试图解释其发生的原因，甚至认为事件其实是可以预测的。这种事后解释现象被称为“后视镜效应”。
    可能会改变我们的信仰和认知：“黑天鹅”事件的出现可能会对人们的信仰和认知产生重大影响，改变我们对现实世界的看法和认识，促使我们重新审视已有的理论和假设。
    在经济学中，“黑天鹅”事件的概念由著名的风险分析学家纳西姆·尼古拉斯·塔勒布（Nassim Nicholas Taleb）所提出。他认为，由于传统的风险管理方法通常只能考虑到已知的风险因素，而无法预测或应对“黑天鹅”事件这种极端情况，因此我们需要更加谨慎和谨慎地处理风险和不确定性。
    """
    def __init__(self):
        self.rare = True
        self.impactful = True
        self.post_hoc_explained = True
        self.mind_changing = True

    def evaluate(self, event):
        if event.is_rare() and event.is_impactful():
            # 对经济系统产生深远的影响
            event.affect_economy()
            if not event.is_predicted():
                # 事后容易被解释
                event.explain_post_hoc()
                # 可能会改变我们的信仰和认知
                event.change_mind()
