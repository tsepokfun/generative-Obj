import GF
import ObjInfo
import ggg
import datetime

Aim = "the tourism of hk in 2008 by info of 2006-2007"
gf = GF.gf()
GOs = ggg.gR("base of this info , " + gf + "Analyze and classify the group of people may appear this aim " + Aim + "point from to list out all object without any other thing")
print(GOs)
GOLs = ggg.gR(GOs + "list it as this this format without enter  /n !!!group N !!!detaill information of this group!!!the memory in first person of this group!!! ")
GO = GOLs.split("!!!")
print("GO list:", GO)

if (len(GO) - 1) % 3 != 0:
    print("Error: The GO list does not have the expected format (groups of 3).")
else:
    i = 1
    while i < len(GO):
        if i + 2 < len(GO):
            group_name = GO[i]
            details = GO[i+1]
            memory = GO[i+2]
            ObjInfo.add(group_name, details, memory)
            print(f"  - Adding GO {group_name} with details: {details}, memory: {memory}")
            i += 3
        else:
            print(f"  - Incomplete group information found near index {i}: {GO[i:]}")
            i += 1

ST = "2008/1/1"
ed = "2008/12/31"

ST_dt = datetime.datetime.strptime(ST, "%Y/%m/%d").date()
ed_dt = datetime.datetime.strptime(ed, "%Y/%m/%d").date()
ct_dt = ST_dt

while ct_dt <= ed_dt:
    ct = ct_dt.strftime("%Y/%m/%d")

    for obj_num in range(ObjInfo.noOfObj):
        obj_data = ObjInfo.getData(obj_num)

        prompt = f"It's {ct}. You are {obj_data[0]}. Your background: {obj_data[1]}. Your memory: {obj_data[2]}. Based on the information: '{GF.gf()}', generate one action that you might do on this date to do with {Aim}. return in this format !!!action!!!time it last"
        action_response = ggg.gR(prompt)  
        if "!!!" in action_response:
            action_parts = action_response.split("!!!")
            action_text = action_parts[1]
            action_duration = action_parts[2]

            GF.adda(ct, obj_num, action_text, action_duration)

            memory_update_prompt = f"It's {ct}. You are {obj_data[0]}. Your background: {obj_data[1]}. Your memory: {obj_data[2]}. You performed the action: '{action_text}'. Update your memory to reflect this. Return only the updated memory."
            updated_memory = ggg.gR(memory_update_prompt)  # Now using caching and backoff
            ObjInfo.upd(obj_num, obj_data[0], obj_data[1], updated_memory)

    ct_dt += datetime.timedelta(days=1)

final_summary = GF.end(Aim, ct)
print("Final Summary:", final_summary)