# Gemini 2.5 Flash VidDiffBench Experiment - Ready to Run

## ✅ **Setup Complete**
- Dataset loaded: 549 samples (easy split)
- Videos downloaded: 4.9GB (surgery + fitness domains)
- Dependencies installed and verified
- No CLIP server needed for Gemini approach

## 🔑 **To Run the Experiment**

### 1. Set Your API Key
```bash
export GEMINI_API_KEY='your-actual-api-key-here'
```

### 2. Run Small Test (2 samples per action)
```bash
python3 lmms/run_lmm.py \
  --config lmms/configs/config.yaml \
  --name gemini_test_small \
  --split easy \
  --eval_mode closed \
  --model models/gemini-2.5-flash-002 \
  --subset_mode 2_per_action
```

### 3. Run Full Easy Split (95 samples)
```bash
python3 lmms/run_lmm.py \
  --config lmms/configs/config.yaml \
  --name gemini_full_easy \
  --split easy \
  --eval_mode closed \
  --model models/gemini-2.5-flash-002 \
  --subset_mode 0
```

### 4. Run All Difficulty Levels
```bash
# Easy split
python3 lmms/run_lmm.py --config lmms/configs/config.yaml --name gemini_easy --split easy --eval_mode closed --model models/gemini-2.5-flash-002 --subset_mode 0

# Medium split  
python3 lmms/run_lmm.py --config lmms/configs/config.yaml --name gemini_medium --split medium --eval_mode closed --model models/gemini-2.5-flash-002 --subset_mode 0

# Hard split
python3 lmms/run_lmm.py --config lmms/configs/config.yaml --name gemini_hard --split hard --eval_mode closed --model models/gemini-2.5-flash-002 --subset_mode 0
```

## 📊 **Results Location**
Results will be saved to:
- `lmms/results/gemini_test_small/` (for small test)
- `lmms/results/gemini_full_easy/` (for full easy split)
- `lmms/results/gemini_easy/` (for easy split)
- etc.

## 🔧 **Configuration Options**

### Evaluation Modes
- `--eval_mode closed`: Multiple choice (a/b) format
- `--eval_mode open`: Free-form text generation

### Subset Modes
- `--subset_mode 0`: All samples in split
- `--subset_mode 2_per_action`: 2 samples per action (for testing)
- `--subset_mode 3_per_action`: 3 samples per action

### Splits
- `--split easy`: 95 samples (easier differences)
- `--split medium`: More difficult differences  
- `--split hard`: Most challenging differences

## 📈 **Performance Expectations**
- **Small test** (2_per_action): ~8 samples, ~2 minutes
- **Full easy split**: 95 samples, ~20-30 minutes
- **All splits**: 549 samples, ~2-3 hours

## 💰 **Cost Estimation (Gemini 2.5 Flash)**
- **Input**: $0.15 per 1M tokens
- **Output**: $0.60 per 1M tokens
- **Estimated cost per sample**: ~$0.01-0.02
- **Full experiment**: ~$5-10 total

## 🔍 **What the Experiment Does**
1. Loads video pairs from VidDiffBench
2. Converts videos to frames at 1 FPS (configurable)
3. Sends video + text prompt to Gemini 2.5 Flash
4. Gemini analyzes differences between video pairs
5. Saves predictions and evaluates against ground truth

## 🎯 **Next Steps**
1. Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Run the small test first to verify everything works
3. Scale up to full experiments based on your needs