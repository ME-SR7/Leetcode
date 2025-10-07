class Solution:
    def interpret(self, command: str) -> str:
        output=[]
        for i in range(len(command)):
            if command[i]=="G":
                output.append("G")

            elif command[i:i+2]=="()":
                output.append("o")
            elif command[i:i+4]=="(al)":
                output.append("al")
            
        return "".join(output)
        