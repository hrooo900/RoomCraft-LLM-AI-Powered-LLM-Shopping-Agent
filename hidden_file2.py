import json 
from langchain_core.messages import AIMessage, ToolMessage

def find_agruments(chunk_list: list, fn_name: str) :
    # print(f"\nhidden_file2:\nFound chunks :\n{chunk_list = }\n","==x=="*5)
    
    
    tool_calls_list = list()

    for i, out_chunk in enumerate(chunk_list):
        if 'agent' in out_chunk:
            if not out_chunk['agent']['messages'][0].content:
                tool_calls_list.extend(out_chunk['agent']['messages'][0].additional_kwargs['tool_calls'])
                print(f"{i= }")
            
            elif i == len(chunk_list)-1 & len(tool_calls_list) == 0:
                return False, "FUNCTIONS ARE NOT CALLED"
                
            
            
    print(f"\n{tool_calls_list  =  }\n\n")
    for tool_used in tool_calls_list:
        if tool_used['function']['name'] == fn_name :
            return True, json.loads(tool_used['function']['arguments'])
        
    return False, 'FUNCTIONS ARE CALLED BUT NOT MATCHED'

