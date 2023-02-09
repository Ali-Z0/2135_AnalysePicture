using System;
using OpenCvSharp;      //inclus la lib OpenCv

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
            //Vas chercher l'immage et ls stock dans img
            Mat img = Cv2.ImRead(@"D:\Utilisateurs\nicolas\Desktop\Projet_POBJ_Reconaissance_Immage_V1\Projet_POBJ_Reconaissance_Immage_V1\images\Surface_blanche_carre_rouge.png");
            //affiche m'immage img originale
            Cv2.ImShow("Original Image", img);

            //Clone l'immage img dans "cloneImg"
            Mat cloneImg = img.Clone();
            //dessine le contour de la forme en blanc (garde que les contours)
            Cv2.Canny(img, cloneImg, 100, 200, 3, false);

            //affiche l'immage des contours de l'immage
            Cv2.ImShow("canny image", cloneImg);
            //attende d'une action par l'utillisateue
            Cv2.WaitKey(0);
        }

        //tests pour reconnaisance de formes
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
