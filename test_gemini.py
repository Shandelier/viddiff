#!/usr/bin/env python3

import os
import sys
import logging

# Add the current directory to the Python path
sys.path.insert(0, ".")

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(filename)s:%(levelname)s:%(message)s")

def test_gemini_setup():
    """Test if Gemini API key is set up"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY environment variable not set")
        print("Please set it with: export GEMINI_API_KEY='your-api-key-here'")
        return False
    print("✅ GEMINI_API_KEY is set")
    return True

def test_dataset_and_videos():
    """Test if dataset and videos are available"""
    try:
        from datasets import load_dataset
        dataset = load_dataset("jmhb/VidDiffBench", cache_dir=None)
        dataset = dataset["test"]
        
        # Filter to easy split with surgery and fitness domains (where we have videos)
        available_domains = ["surgery", "fitness"]
        easy_dataset = dataset.filter(lambda x: x["split"] == "easy" and x["domain"] in available_domains)
        
        print(f"✅ Dataset loaded: {len(easy_dataset)} samples from easy split (surgery & fitness)")
        
        # Check if video files exist
        import os
        surgery_path = "data/src_jigsaws"
        fitness_path = "data/src_humman"
        
        if os.path.exists(surgery_path) and os.path.exists(fitness_path):
            print("✅ Video files are available")
            return True, easy_dataset
        else:
            print("❌ Video files not found")
            return False, None
            
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return False, None

def run_gemini_test():
    """Run a simple test with Gemini 2.5 Flash"""
    print("\n=== Testing Gemini 2.5 Flash with VidDiffBench ===")
    
    # Check setup
    if not test_gemini_setup():
        return False
    
    success, dataset = test_dataset_and_videos()
    if not success:
        return False
    
    # Try to run a simple LMM test
    try:
        print("\n🚀 Running Gemini 2.5 Flash test...")
        print("Command to run:")
        print("python3 lmms/run_lmm.py --config lmms/configs/config.yaml --name gemini_test --split easy --eval_mode closed --model models/gemini-2.5-flash-002")
        
        # Note: We're not actually running this here to avoid API costs
        # But this shows the user how to run it
        print("\n📝 To run the actual test, execute the command above")
        print("This will:")
        print("1. Load the easy split dataset")
        print("2. Use Gemini 2.5 Flash to analyze video differences")
        print("3. Evaluate the model's performance")
        print("4. Save results to lmms/results/gemini_test/")
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up test: {e}")
        return False

def main():
    print("VidDiffBench Gemini 2.5 Flash Test Setup")
    print("=" * 50)
    
    if run_gemini_test():
        print("\n✅ Setup complete! You can now run Gemini 2.5 Flash with VidDiffBench")
        print("\nNext steps:")
        print("1. Set your GEMINI_API_KEY if not already done")
        print("2. Run the test command shown above")
        print("3. Check results in lmms/results/")
    else:
        print("\n❌ Setup failed. Please check the errors above.")

if __name__ == "__main__":
    main()