import GF
import ObjInfo
import ggg
import datetime

Aim = "the tourism of hk in 2008 by info of 2006-2007"

print("Step 1: Getting initial fact data")
gf = GF.gf()
print("  - Fact data retrieved:", gf)

print("Step 2: Analyzing and classifying groups of people (GOs)")
GOs = ggg.gR("base of this info , " + gf + "Analyze and classify the group of people may appear this aim " + Aim + "point from to list out all object without any other thing")
print("  - Groups of people (GOs) identified:", GOs)

print("Step 3: Getting detailed information and memory for each GO")
GOLs = ggg.gR(GOs + "list it as this this format without enter  /n !!!group N !!!detaill information of this group!!!the memory in first person of this group!!! ")
GO = GOLs.split("!!!")
print("  - Raw detailed information and memory string:", GOLs)

print("Step 4: Adding GOs to ObjInfo")
for i in range(1, len(GO), 3):
    print(f"  - Adding GO {GO[i]} with details: {GO[i+1]}, memory: {GO[i+2]}")
    ObjInfo.add(GO[i], GO[i+1], GO[i+2])

ST = "2008/1/1"
ed = "2008/12/31"

ST_dt = datetime.datetime.strptime(ST, "%Y/%m/%d").date()
ed_dt = datetime.datetime.strptime(ed, "%Y/%m/%d").date()
ct_dt = ST_dt

print("Step 5: Entering main simulation loop")
while ct_dt <= ed_dt:
    ct = ct_dt.strftime("%Y/%m/%d")
    print(f"\n--- Current Date: {ct} ---")

    for obj_num in range(ObjInfo.noOfObj):
        print(f"  - Processing GO number: {obj_num}")
        obj_data = ObjInfo.getData(obj_num)
        print(f"    - GO Data: {obj_data}")

        prompt = f"It's {ct}. You are {obj_data[0]}. Your background: {obj_data[1]}. Your memory: {obj_data[2]}. Based on the information: '{GF.gf()}', generate one action that you might do on this date to do with {Aim}. return in this format !!!action!!!time it last"
        print(f"    - Prompt sent to LLM: {prompt}")

        action_response = ggg.gR(prompt)
        print(f"    - Action response from LLM: {action_response}")

        if "!!!" in action_response:
            action_parts = action_response.split("!!!")
            action_text = action_parts[1]
            action_duration = action_parts[2]
            print(f"    - Parsed action: {action_text}, Duration: {action_duration}")

            GF.adda(ct, obj_num, action_text, action_duration)
            print(f"    - Action added to timeline (GF.adda)")

            memory_update_prompt = f"It's {ct}. You are {obj_data[0]}. Your background: {obj_data[1]}. Your memory: {obj_data[2]}. You performed the action: '{action_text}'. Update your memory to reflect this. Return only the updated memory."
            print(f"    - Memory update prompt: {memory_update_prompt}")

            updated_memory = ggg.gR(memory_update_prompt)
            print(f"    - Updated memory from LLM: {updated_memory}")

            ObjInfo.upd(obj_num, obj_data[0], obj_data[1], updated_memory)
            print(f"    - GO memory updated in ObjInfo")
        else:
            print(f"    - No action parsed for GO {obj_num} on {ct}")

    ct_dt += datetime.timedelta(days=1)

print("\nStep 6: Generating final summary")
final_summary = GF.end(Aim, ct)
print("  - Final Summary:", final_summary)