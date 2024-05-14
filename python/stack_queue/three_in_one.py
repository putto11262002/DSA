
class Stacks: 
    def __init__(self, num_stacks) -> None:
        self.stack_cap = 5;
        self.num_stacks = num_stacks
        self.values = [0] * (self.stack_cap * self.num_stacks)
        self.sizes = [0] * self.num_stacks

    def get_start_idx(self, stack): 
        return (self.stack_cap * (stack - 1))

    def is_valid_stack(self, stack): 
        return stack < 1 or stack > self.num_stacks
    
    def push(self, stack: int, value: int): 

        if self.is_valid_stack(stack): 
            raise ValueError("Invalid stack")
       
       
        if self.is_full(stack):
            print(f'Stack {stack} has reached its maximum capacity')
            return  
        
        idx = self.get_start_idx(stack) + (self.sizes[stack - 1])
        self.values[idx] = value
        self.sizes[stack - 1] += 1

    
    def pop(self, stack: int): 
        if stack < 1 or stack > self.num_stacks: 
            raise ValueError("Invalid stack")
        if self.is_empty(stack): 
            raise ValueError("Stack is empty")
        
        idx = self.get_start_idx(stack) + self.sizes[stack - 1] -1
        value = self.values[idx]
        self.sizes[stack -1] -= 1
        return value
    
    def peek(self, stack: int): 
        if stack < 1 or stack > self.num_stacks: 
            raise ValueError("Invalid stack")
        if self.is_empty(stack):
            raise ValueError("Stack is empty")
        idx = self.get_start_idx(stack) + self.sizes[stack - 1] - 1
        value  = self.values[idx]
        return value
    
    def is_empty(self, stack: int): 
        if stack < 1 or stack > self.num_stacks: 
            print("Invalid stack")
            return 
        return self.sizes[stack - 1] < 1
    
    def is_full(self, stack: int): 
        return self.sizes[stack - 1] == self.stack_cap
        

    
    def __str__(self): 
       
        parts = []
        for stack in range(1, self.num_stacks + 1): 

            start_idx = self.get_start_idx(stack)
            parts.append(f'Stack {stack}: ')
            parts.append(str(self.values[start_idx:start_idx + self.sizes[stack - 1]]))
            parts.append("\n")
        
        return "".join(parts)











        

        


    
