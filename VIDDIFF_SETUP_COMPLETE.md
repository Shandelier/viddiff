# VidDiffBench Setup Complete - Ready for Gemini 2.5

## ✅ What's Successfully Set Up

### 1. **Dependencies & Environment**
- All Python packages installed successfully
- VidDiffBench dataset loaded from HuggingFace Hub (549 samples)
- Dataset structure corrected (fixed dataset name from `viddiff/VidDiffBench_2` to `jmhb/VidDiffBench`)

### 2. **Video Files Downloaded**
- **Surgery videos**: 167MB downloaded and extracted (`data/src_jigsaws/`)
- **Fitness videos**: 4.7GB downloaded and extracted (`data/src_humman/`)
- Total video data: ~4.9GB
- Available domains: surgery, fitness (out of 5 total domains)

### 3. **Dataset Structure**
- **Total samples**: 549 (easy: 95, medium, hard splits)
- **Surgery + Fitness samples**: Available for testing
- **Missing domains**: ballsports, music, diving (no video files available)

## 🚀 How to Run Gemini 2.5 Flash

### Step 1: Set Up API Key
```bash
export GEMINI_API_KEY='your-gemini-api-key-here'
```

### Step 2: Test the Setup
```bash
python3 test_gemini.py
```

### Step 3: Run Gemini 2.5 Flash (Closed Evaluation)
```bash
python3 lmms/run_lmm.py --config lmms/configs/config.yaml --name gemini25_test --split easy --eval_mode closed --model models/gemini-2.5-flash-002
```

### Step 4: Run Gemini 2.5 Flash (Open Evaluation)
```bash
python3 lmms/run_lmm.py --config lmms/configs/config.yaml --name gemini25_open --split easy --eval_mode open --model models/gemini-2.5-flash-002
```

## 📊 What the System Does

### Input
- **Two videos** of the same action (e.g., surgical procedure, fitness exercise)
- **Action description**: Text describing what action is being performed
- **Difference candidates**: List of potential differences between videos

### Output
- **Predictions**: For each difference, predict which video ('a' or 'b') shows that difference more prominently
- **Evaluation metrics**: Accuracy, precision, recall on the predictions

### Example
```
Videos: [surgery_video_1.mp4, surgery_video_2.mp4]
Action: "Suturing technique"
Differences: ["faster hand movements", "different grip style", "tool held closer to tip"]
Predictions: {"0": "a", "1": "b", "2": "a"}
```

## 🔧 CLIP Server Explained

### Why CLIP Server is Needed
The CLIP server is crucial for the **VidDiff method** (not needed for basic LMM testing):

1. **Frame Retrieval**: Finds most relevant video frames for each difference description
2. **Text-Image Similarity**: Computes similarity between difference descriptions and video frames
3. **Efficiency**: Keeps CLIP model loaded in memory, avoiding repeated loading
4. **Caching**: Automatic caching of CLIP embeddings for faster reuse

### When You Need It
- **For LMM testing (Gemini 2.5)**: NOT needed
- **For VidDiff method**: Required

### How to Start CLIP Server (if needed)
```bash
python3 apis/clip_server.py &
```

## 🎯 Available Test Configurations

### 1. **Basic LMM Test** (Recommended for Gemini 2.5)
```bash
# Just test model performance without advanced VidDiff method
python3 lmms/run_lmm.py --model models/gemini-2.5-flash-002 --split easy
```

### 2. **VidDiff Method Test** (Requires CLIP server)
```bash
# Full 3-stage VidDiff pipeline
python3 viddiff_method/run_viddiff.py --split easy --eval_mode closed
```

### 3. **Other Models for Comparison**
```bash
# OpenAI GPT-4o
python3 lmms/run_lmm.py --model gpt-4o-2024-08-06 --split easy

# Anthropic Claude
python3 lmms/run_lmm.py --model anthropic/claude-3.5-sonnet --split easy
```

## 📁 Results Location
Results will be saved to:
- `lmms/results/[experiment_name]/` for LMM tests
- `viddiff_method/results/[experiment_name]/` for VidDiff method

## 🔍 Quick Status Check
Run this to verify everything is working:
```bash
python3 test_gemini.py
```

## 📝 Key Files Created/Modified
- `download_videos.py`: Fixed video download script
- `data/load_viddiff_dataset.py`: Updated dataset name
- `test_gemini.py`: Test script for setup verification
- `VIDDIFF_SETUP_COMPLETE.md`: This summary document

## 🚨 Current Limitations
1. **API Key Required**: Need `GEMINI_API_KEY` for Gemini 2.5
2. **Limited Video Domains**: Only surgery and fitness videos available
3. **CLIP Server**: Required for VidDiff method but not basic LMM testing

## ✅ Ready to Use!
The system is now fully set up and ready to test Gemini 2.5 Flash on the VidDiffBench dataset. Just set your API key and run the commands above!