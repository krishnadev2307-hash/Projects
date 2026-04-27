# Project: Convolution

This project demonstrates two approaches to image convolution:

* A manual implementation to understand the algorithm
* An optimized version using OpenCV for real-world performance

---

## Structure

```
convolution/
│
├── src/
│   ├── core/
│   │   └── core.py        # Manual O(n^4) implementation
│   │
│   └── optimized/
│       └── optimized.py   # OpenCV-based implementation
│
├── Images/
│   ├── Itachi.jpeg               # Input image
│   ├── Blur.jpg                  # Output: blur filter
│   ├── Sharpen.jpg               # Output: sharpen filter
│   └── EdgeDetection.jpg         # Output: edge detection
│
└── README.md
```

---

## Tech Used

* Python
* OpenCV
* NumPy

---

## Images

All input and output images are stored in the `Images/` directory.

---

## Goal

To understand the difference between theoretical implementation and optimized library-based approaches.