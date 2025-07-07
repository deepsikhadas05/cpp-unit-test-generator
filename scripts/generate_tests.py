import os
import yaml
import subprocess

# ========== CONFIG ==========
SRC_DIR = "../orgChartApi"
YAML_PROMPT_PATH = "../yaml_prompts/generate_tests.yaml"
OUTPUT_DIR = "../tests/"
OLLAMA_MODEL = "phi"  # or any model you’ve pulled with `ollama pull llama3`
# ============================

def load_yaml_prompt(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def read_cpp_files(src_path):
    cpp_data = ""
    for filename in os.listdir(src_path):
        if filename.endswith(".cpp"):
            with open(os.path.join(src_path, filename), 'r') as f:
                cpp_data += f"\n\n// File: {filename}\n" + f.read()
    return cpp_data

def build_prompt(yaml_prompt, cpp_code):
    instructions = yaml.dump(yaml_prompt)
    return f"""### YAML INSTRUCTION:
{instructions}

### C++ SOURCE CODE:
{cpp_code}

### TASK:
Generate Google Test-based unit test files for the given source code using the above instructions. Output only C++ test code, separated by file if necessary.
"""

def call_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", OLLAMA_MODEL],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode()

def save_tests_to_output(output_text):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 1
    for section in output_text.split('// File:'):
        if "TEST" in section or "TEST_F" in section:
            filename = f"test_file_{count}.cpp"
            with open(os.path.join(OUTPUT_DIR, filename), 'w') as f:
                f.write("// File:" + section.strip())
            count += 1

def main():
    print("📄 Loading prompt and source...")
    prompt_yaml = load_yaml_prompt(YAML_PROMPT_PATH)
    cpp_code = read_cpp_files(SRC_DIR)
    full_prompt = build_prompt(prompt_yaml, cpp_code)

    print("🤖 Sending to Ollama...")
    output = call_ollama(full_prompt)

    print("💾 Saving test files...")
    save_tests_to_output(output)

    print(f"✅ Done! Tests saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
