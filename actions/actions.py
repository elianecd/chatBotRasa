# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionValidarEspecialidade(Action):

    def name(self) -> Text:
        return "action_validar_especialidade"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Pegar o valor da especialidade no slot
        especialidade = tracker.get_slot("especialidade_medico")
        data = tracker.get_slot("data_hora_consulta")
        periodo = tracker.get_slot("periodo_consulta_agenda")

        # Lista de especialidades válidas
        especialidades_validas = ["nutricionista", "cardiologia", "endocrino", "ortopedista"]

        print("foi")

        # Verificar se a especialidade é válida
        if especialidade.lower() in especialidades_validas:
            dispatcher.utter_message(text=f"Especialidade confirmada para atendimento. Iremos encaminhar esses dados para a nossa central:\n- {especialidade}\n- {data}\n- {periodo}.\nMais tarde entraremos em contato. Posso ajudar com mais alguma coisa?")
            return []
        else:
            dispatcher.utter_message(text=f"Desculpe, essa especialidade não está disponível. As especialidades disponíveis são: {', '.join(especialidades_validas)}. Favor digitar 'Quero agendar uma consulta' para reiniciar o diálogo se desejar.")
            return [SlotSet("especialidade_medico", None)]