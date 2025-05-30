from enum import Enum


class AgentTypeEnum(str, Enum):
    banking_payment_agent = "banking_payment_agent"
    banking_payment_subagent = "banking_payment_subagent"
    payment_agent = "payment_agent"
    payment_subagent = "payment_subagent"
    attorney = "attorney"
    commissioner = "commissioner"
    agent = "agent"
