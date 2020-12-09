from typing import List, Union
import copy


class LoopDetectedError(Exception):
    value: int
    message: str

    def __init__(self, value):
        self.value = value
        self.message = "Loop Detected"


class EndOfProgram(Exception):
    value: int
    message: str

    def __init__(self, value):
        self.value = value
        self.message = "Program Completed"


class Console:
    accumulator: int = 0
    ptr: int = 0
    program: List[str]
    history: List[int]

    def __init__(self, program: List[str]):
        self.program = copy.deepcopy(program)
        self.history = [0 for x in self.program]

    def run(self):
        while True:
            try:
                # Loop Detector
                if self.history[self.ptr] != 0:
                    raise LoopDetectedError(self.accumulator)
                self.history[self.ptr] += 1

                # Run Execution
                instruction = self.program[self.ptr]
                self.call(instruction)
                self.ptr += 1
            except IndexError:
                raise EndOfProgram(self.accumulator)

    def call(self, instruction):
        op, val = instruction.split(" ")

        try:
            getattr(self, op)(val)
        except AttributeError:
            pass

    def acc(self, val: Union[str, int]):
        self.accumulator += int(val)

    def jmp(self, val: Union[str, int]):
        # Remove 1 from jump call to prevent extra step
        self.ptr += int(val) - 1

    def nop(self, val: Union[str, int]):
        pass

    def edit(self, idx, op=None, val=None):
        new_op, new_val = self.program[idx].split(" ")
        if op is not None:
            new_op = op
        if val is not None:
            new_val = str(val)

        self.program[idx] = f"{new_op} {new_val}"
