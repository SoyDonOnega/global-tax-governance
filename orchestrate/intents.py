"""Closed enum of handoff intents. Importable from any Python tool.

Three intents are defined. Skills run self-contained recipes and only
delegate to the shared critics for the disciplinary review pass:

  - critic_check          · skill asks one of the six transversal critics
                            to review a deliverable
  - request_clarification · the active skill needs information from the
                            user before continuing
  - escalate_to_human     · a finding requires human review before publish
"""
from enum import Enum


class Intent(str, Enum):
    CRITIC_CHECK          = "critic_check"
    REQUEST_CLARIFICATION = "request_clarification"
    ESCALATE_TO_HUMAN     = "escalate_to_human"


ALL_INTENTS = [i.value for i in Intent]
