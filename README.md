# 🔥 Complete CUDA to PyTorch Installation Guide

## 📊 How to Find Your CUDA Version

Run this command in PowerShell:

```powershell
nvidia-smi
```

**Look at the top-right corner of the output:**

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 580.97                 Driver Version: 580.97    CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
                                                                    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                                                                    THIS NUMBER!
```

---

## 📋 Complete CUDA Version to PyTorch Installation Table

| CUDA Version (from nvidia-smi) | PyTorch Installation Command | Notes |
|-------------------------------|------------------------------|-------|
| **13.0** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124` | ✅ Use CUDA 12.4 build (backward compatible) |
| **12.6** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124` | ✅ Use CUDA 12.4 build |
| **12.5** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124` | ✅ Use CUDA 12.4 build |
| **12.4** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124` | ✅ Perfect match |
| **12.3** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` | ✅ Use CUDA 12.1 build |
| **12.2** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` | ✅ Use CUDA 12.1 build |
| **12.1** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` | ✅ Perfect match |
| **12.0** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` | ✅ Use CUDA 12.1 build |
| **11.8** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` | ✅ Perfect match |
| **11.7** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` | ✅ Use CUDA 11.8 build |
| **11.6** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` | ✅ Use CUDA 11.8 build |
| **11.5** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` | ✅ Use CUDA 11.8 build |
| **11.4 or lower** | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` | ⚠️ Works but consider updating drivers |
| **10.x or lower** | `pip install torch torchvision torchaudio` | ⚠️ CPU-only fallback (very old drivers) |
| **No NVIDIA GPU** | `pip install torch torchvision torchaudio` | ℹ️ CPU-only mode |

---

## 🎯 Quick Decision Tree

### Step 1: Check Your CUDA Version

```powershell
nvidia-smi
```

### Step 2: Choose Your Command

```
CUDA 13.0, 12.4-12.6  → Use cu124
CUDA 12.0-12.3        → Use cu121
CUDA 11.4-11.8        → Use cu118
CUDA 11.3 or lower    → Use cu118 (but update drivers!)
No NVIDIA GPU         → Use CPU-only
```

### Step 3: Install PyTorch

**For CUDA 12.4+ (including 13.0):**
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

**For CUDA 12.0-12.3:**
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**For CUDA 11.x:**
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**For CPU-only (no GPU or very old drivers):**
```powershell
pip install torch torchvision torchaudio
```

---

## 🔍 Understanding CUDA Compatibility

### Important Notes:

1. **Backward Compatibility:** Higher CUDA versions can use older PyTorch CUDA builds
   - Example: CUDA 13.0 works perfectly with cu124 (CUDA 12.4 build)

2. **Forward Compatibility:** Older CUDA versions **CANNOT** use newer PyTorch CUDA builds
   - Example: CUDA 11.8 cannot use cu124 (will fail!)

3. **Sweet Spot Versions:**
   - **cu124** = Best for CUDA 12.4+ (most modern GPUs)
   - **cu121** = Best for CUDA 12.0-12.3
   - **cu118** = Best for CUDA 11.x (older GPUs)

---

## ✅ Verification After Installation

### Step 1: Check if PyTorch Detects Your GPU

```powershell
python -c "import torch; print('CUDA Available:', torch.cuda.is_available())"
```

**Expected Output:**
```
CUDA Available: True
```

### Step 2: Check GPU Name

```powershell
python -c "import torch; print('GPU:', torch.cuda.get_device_name(0))"
```

**Expected Output:**
```
GPU: NVIDIA GeForce RTX 4060
```

### Step 3: Check CUDA Version PyTorch is Using

```powershell
python -c "import torch; print('PyTorch CUDA Version:', torch.version.cuda)"
```

**Expected Output:**
```
PyTorch CUDA Version: 12.4
```

---

## 🔧 What If You Installed the Wrong Version?

### Fix: Uninstall and Reinstall

```powershell
# Step 1: Uninstall current PyTorch
pip uninstall torch torchvision torchaudio

# Step 2: Install correct version (use your CUDA version from table above)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Step 3: Verify
python -c "import torch; print('CUDA Available:', torch.cuda.is_available())"
```

---

## 📊 Real-World Examples

### Example 1: Modern Gaming PC (RTX 4060)
```
nvidia-smi shows: CUDA Version: 13.0
Command to use: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
Result: ✅ Works perfectly
```

### Example 2: Laptop with RTX 3060
```
nvidia-smi shows: CUDA Version: 12.2
Command to use: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
Result: ✅ Works perfectly
```

### Example 3: Older Desktop with GTX 1060
```
nvidia-smi shows: CUDA Version: 11.8
Command to use: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
Result: ✅ Works perfectly
```

### Example 4: Laptop without NVIDIA GPU (Intel/AMD graphics)
```
nvidia-smi: Command not found
Command to use: pip install torch torchvision torchaudio
Result: ✅ Works but uses CPU (slower)
```

---

## 🚨 Common Mistakes to Avoid

### ❌ Mistake #1: Using cu124 with CUDA 11.x
```powershell
# DON'T DO THIS if you have CUDA 11.8:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
**Result:** PyTorch won't detect your GPU!

### ❌ Mistake #2: Not Checking CUDA Version First
**Always run `nvidia-smi` BEFORE installing PyTorch!**

### ❌ Mistake #3: Installing CPU Version When You Have GPU
```powershell
# DON'T DO THIS if you have NVIDIA GPU:
pip install torch torchvision torchaudio
```
**Result:** Unnecessarily slow processing (no GPU acceleration)

---

## 💡 Pro Tips

### Tip 1: Update Your NVIDIA Drivers
If you have an old CUDA version (11.x), consider updating:
1. Go to: https://www.nvidia.com/download/index.aspx
2. Download latest driver for your GPU
3. Install and restart
4. Run `nvidia-smi` again to see new CUDA version

### Tip 2: When in Doubt, Use One Version Lower
If you have CUDA 13.0 but cu124 doesn't work, try cu121:
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### Tip 3: Save Your Working Command
Once you find the command that works, save it somewhere:
```
My GPU: RTX 4060
My CUDA: 13.0
Working command: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

---

## 🎯 Summary Cheat Sheet

| If `nvidia-smi` shows | Use this command |
|----------------------|------------------|
| CUDA 12.4 - 13.x | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124` |
| CUDA 12.0 - 12.3 | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121` |
| CUDA 11.x | `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118` |
| No GPU / Error | `pip install torch torchvision torchaudio` |

---

**Last Updated:** October 2025  
**PyTorch Version:** 2.x+  
**Tested CUDA Versions:** 11.8, 12.1, 12.4, 13.0
