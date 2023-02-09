using System;
using OpenCvSharp;
//using Emgu.CV;
//using Emgu.CV.CvEnum;
//using Emgu.CV.Structure;
//using System.Drawing;


namespace Projet_POBJ_Reconaissance_Immage_V1
{
    class Program
    {
        static void Main(string[] args)
        {
            LoadAndDisplayImage();
        }
        static void LoadAndDisplayImage()
        {
            //         string imagePath = string.Format(@"C:\Users\pf85ges\source\repos\Projet_POBJ_Reconaissance_Immage_V1\Projet_POBJ_Reconaissance_Immage_V1\images\Surface_blanche_carre_rouge.png", AppDomain.CurrentDomain.BaseDirectory);
            //         Mat colorImage = Cv2.ImRead(imagePath, ImreadModes.Color);

            //Point[][] contours = GetContours(colorImage);
            //         Mat imageContour = colorImage.Clone();
            //         Cv2.DrawContours(imageContour, contours, -1, new Scalar(0, 0, 0), thickness: 3);




            //         Cv2.ImShow("Contours de l'image", colorImage);
            //         Cv2.ImShow("Contours de l'image", imageContour);
            //         Cv2.WaitKey();

            Mat img = Cv2.ImRead(@"C:\Users\pf85ges\source\repos\Projet_POBJ_Reconaissance_Immage_V1\Projet_POBJ_Reconaissance_Immage_V1\images\Surface_blanche_carre_rouge.png");
            Cv2.ImShow("Original Image", img);
            Cv2.GaussianBlur(img, img, new Size(3, 3), 1);
            //Cv2.WaitKey(0);

            Mat coins = img.Clone(); ;
            Cv2.Canny(img, coins, 100, 200, 3, false);


            Cv2.ImShow("canny image", coins);
            Cv2.WaitKey(0);

            //  Pour avancer, regarde ca :
            //  https://www.emgu.com/wiki/index.php/Shape_(Triangle,_Rectangle,_Circle,_Line)_Detection_in_CSharp
            //  voilà
        }

        static Point[][] GetContours(Mat _immage)
        {
            Mat imgGray = new Mat();
            Cv2.CvtColor(_immage, imgGray, ColorConversionCodes.BGR2GRAY);
            Mat bordures = new Mat();
            Cv2.Threshold(imgGray, bordures, 127, 255, ThresholdTypes.Binary);

            Point[][] contours;
            HierarchyIndex[] indexe;
            Cv2.FindContours(bordures, out contours, out indexe, RetrievalModes.List, ContourApproximationModes.ApproxSimple);

            return contours;
        }
	}
}
