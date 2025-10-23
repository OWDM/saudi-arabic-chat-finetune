import json

# Input files
jsonl_file = r"/home/Musaed/Documents/GitHub/saudi-arabic-chat-finetune/chunk1.jsonl"
prompt_file = r"/home/Musaed/Documents/GitHub/saudi-arabic-chat-finetune/prompt.txt"
output_file = r"/home/Musaed/Documents/GitHub/saudi-arabic-chat-finetune/merged2.jsonl"

# Read the system prompt
with open(prompt_file, "r", encoding="utf-8") as f:
    system_prompt = f.read().strip()

# Open input and output files
with open(jsonl_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        data = json.loads(line)
        prompt = data["prompt"]
        completion = data["completion"]

        merged = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": completion}
            ]
        }

        outfile.write(json.dumps(merged, ensure_ascii=False) + "\n")

print(f"✅ Merged file saved as: {output_file}")
