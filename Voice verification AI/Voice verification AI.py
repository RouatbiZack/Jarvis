import numpy as np
import librosa
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load audio data
# Replace this with your own audio data, loaded into a list of arrays, where each array represents a single audio recording
audio_data = ...

# Extract MFCC features from audio data
mfcc_features = []
for audio in audio_data:
    mfccs = librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=13)
    mfcc_features.append(mfccs.mean(axis=1))

# Convert MFCC features to a 2D array
mfcc_features = np.array(mfcc_features)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(mfcc_features, labels, test_size=0.2)

# Train a SVM classifier
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(acc * 100))
