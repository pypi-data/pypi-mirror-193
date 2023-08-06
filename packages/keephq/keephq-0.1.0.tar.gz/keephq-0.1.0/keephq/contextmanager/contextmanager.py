from typing import Self

import click


class ContextManager:
    __instance = None

    # https://stackoverflow.com/questions/36286894/name-not-defined-in-type-annotation
    @staticmethod
    def get_instance() -> "ContextManager":
        if ContextManager.__instance == None:
            ContextManager()
        return ContextManager.__instance

    def __init__(self):
        if ContextManager.__instance != None:
            raise Exception(
                "Singleton class is a singleton class and cannot be instantiated more than once."
            )
        else:
            ContextManager.__instance = self

        self.steps_context = {}
        self.providers_context = {}
        self.alerts_context = {}
        self.foreach_context = {}
        self.click_context = click.get_current_context()

    def get_full_context(self):
        return {
            "providers": self.providers_context,
            "steps": self.steps_context,
            "foreach": {"value": self.foreach_context},
        }

    def set_for_each_context(self, value):
        self.foreach_context = value

    def get_key(self, key):
        context = self.context_manager.get_full_context()
        key = key.strip()
        for k in key.split("."):
            if k in context:
                context = context[k]
            else:
                return None
        # strip quotes TODO - better way to do this (should be a trim function)
        return context

    def set_condition_results(
        self, step_id, condition_id, raw_value, compare_to, compare_value, result
    ):
        if step_id not in self.steps_context:
            self.steps_context[step_id] = {"conditions": {}, "results": {}}
        if "conditions" not in self.steps_context[step_id]:
            self.steps_context[step_id]["conditions"] = {}

        if condition_id not in self.steps_context[step_id]["conditions"]:
            self.steps_context[step_id]["conditions"][condition_id] = []

        self.steps_context[step_id]["conditions"][condition_id].append(
            {
                "raw_value": raw_value,
                "value": compare_value,
                "compare_to": compare_to,
                "result": result,
            }
        )

    def get_actionable_results(self):
        actionable_results = []
        for step_id in self.steps_context:
            if "conditions" in self.steps_context[step_id]:
                for condition_id in self.steps_context[step_id]["conditions"]:
                    for condition in self.steps_context[step_id]["conditions"][
                        condition_id
                    ]:
                        if condition["result"] == True:
                            actionable_results.append(
                                {
                                    "step_id": step_id,
                                    "condition_id": condition_id,
                                    "condition": condition,
                                }
                            )
        return actionable_results
