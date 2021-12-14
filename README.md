## Table of Contents

- [Summary](#summary)
- [Data Collection](#data-collection)
- [Testing](#testing)
- [Contribution](#contribution)

## Summary

This Android application, based on [Google's ML Kit](https://github.com/googlesamples/mlkit), uses a TensorFlow model built on the basis of a collection of images. It detects and tries to label cars, and these labels comprise car models from different manufacturers.

## Data Collection

All of these images are Creative Commons images, and were manually downloaded and collected in the `cars` directory.

## Testing

This application is best tested using Android Studio, and [this link](https://developer.android.com/studio/run) provides information on how to run the application itself, and [this link](https://developer.android.com/studio/run/device) provides sufficient information to test the application on an Android mobile device.

## Contribution

If you want to contribute to this application, it can be in two ways: adding data or improving the way the model is made in `modelcreate.py`. This should be done using the two branches that pertain to each way of contribution.
