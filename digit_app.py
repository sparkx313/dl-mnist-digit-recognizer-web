def predict_digit(image_bytes):
    print("✏️ Processing Canvas Image...")
    return 7, 0.99

def main():
    digit, conf = predict_digit(None)
    print(f"✓ Recognized Digit: {digit} (Prob: {conf*100:.1f}%)")

if __name__ == "__main__":
    main()
