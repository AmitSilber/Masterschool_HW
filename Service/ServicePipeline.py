from abc import abstractmethod

from Service import globals


class StagePipeline:
    def __init__(self, pipeline, stage_class):
        """

        @param pipeline: a list of all stages to complete
        @param stage_class: the class representing the stage
        """
        self._stages_pipeline = []
        self._status = globals.PENDING
        self._stage_index = 0
        self._parse_pipeline(pipeline, stage_class)

    def _parse_pipeline(self, pipeline, stage_class):
        for stage in pipeline:
            parsed_service = stage_class(stage)
            self._stages_pipeline.append(parsed_service)

    @abstractmethod
    def get_flow(self):
        """
        check if completed,
        else return status according to the specific class
        @return: dict representing the process with the current state
        """
        pass

    @abstractmethod
    def _validate_input(self, argument):
        """

        @param argument: input arguments for stages
        @return: true or false depending on the validity
        """
        pass

    @abstractmethod
    def update_pipeline(self, arguments):
        """
        do checks of validation and state of pipeline,
        then update the pipeline if necessary finally do _update_status
        @param arguments: input arguments for stages
        @return: dict with the current state and the assessment of validate_input function
        """

        pass

    @abstractmethod
    def _update_status(self, stage_status):
        """
        update status given the status of the stage. If failed then we reject,
        otherwise we advance and keep in mind the possibility of completing all stages
        @param stage_status:
        @return: None
        """
        pass
