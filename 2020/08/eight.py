# sample answer is 5

class Program(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.running = False
        self.instruction_executions = [0] * len(self.instructions)
        self.accumulator = 0
        self.current_position = 0

    def run_instruction(self, instruction):
        inst, value = instruction.split(' ')
        self.instruction_executions[self.current_position] += 1
        if self.instruction_executions[self.current_position] == 2:
            self.running = False
            return
        if inst == 'acc':
            if value[0] == '+':
                self.accumulator += int(value[1:])
            elif value[0] == '-':
                self.accumulator -= int(value[1:])
            self.current_position += 1            
        if inst == 'nop':
            self.current_position += 1
        if inst == 'jmp':
            if value[0] == '+':
                self.current_position += int(value[1:])
            elif value[0] == '-':
                self.current_position -= int(value[1:])

    def run_program(self):
        self.running = True
        self.exit = 1
        while self.running:
            self.run_instruction(self.instructions[self.current_position])
            if self.current_position == len(self.instructions):
                self.exit = 0
                break
        return self.exit, self.accumulator

def main():
    boot_path = 'eight.input'
    with open(boot_path, 'r') as f:
        instructions = [tmp.replace('\n', '') for tmp in f.readlines()]
    print(instructions)
    print()
    for i in range(0, len(instructions)):
        if 'nop' in instructions[i]:
            instructions[i] = instructions[i].replace('nop', 'jmp')
        elif 'jmp' in instructions[i]:
            instructions[i] = instructions[i].replace('jmp', 'nop')
        P = Program(instructions)
        exit_status, accumulator = P.run_program()
        if exit_status == 0:
            print(instructions)
            print(accumulator)
            break
        else:
            if 'nop' in instructions[i]:
                instructions[i] = instructions[i].replace('nop', 'jmp')
            elif 'jmp' in instructions[i]:
                instructions[i] = instructions[i].replace('jmp', 'nop')

if __name__ == "__main__":
    main()