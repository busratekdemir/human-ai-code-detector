import unittest
import joblib
import os

class HumanAICodeDetectorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(base_dir, ".."))

        cls.model_path = os.path.join(project_root, "app", "LogisticRegression.pkl")
        cls.vectorizer_path = os.path.join(project_root, "app", "vectorizer.pkl")

    def testCase01ModelLoad_model(self):
        self.assertTrue(os.path.exists(self.model_path), "model dosyası bulunamadı!")
        model = joblib.load(self.model_path)
        self.assertIsNotNone(model, "model yüklemesi yapılamadı")

    def testCase02VectorTest(self):
        self.assertTrue(os.path.exists(self.vectorizer_path), "vectorizer dosyası bulunamadı!")
        vectorizer = joblib.load(self.vectorizer_path)
        test_kod = ["public static void main(String[] args) {}"]
        vektor = vectorizer.transform(test_kod)

        # eğitim ayarından bağımsız, sağlam kontrol
        self.assertGreater(vektor.shape[1], 0, "vektör boş geldi!")

    def test_case_03_prediction_logic(self):
        model = joblib.load(self.model_path)
        vectorizer = joblib.load(self.vectorizer_path)
        X = vectorizer.transform(["def test_function(): pass"])
        tahmin = model.predict(X)[0]

        # insan / yapay zeka sınıfları
        self.assertIn(tahmin, [0, 1], "tahmin sınıfı geçerli değil!")

if __name__ == '__main__':
    unittest.main()