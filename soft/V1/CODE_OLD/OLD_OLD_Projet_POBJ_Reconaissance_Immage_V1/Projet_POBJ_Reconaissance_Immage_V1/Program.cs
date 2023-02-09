using System;
using OpenCvSharp;

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
            string imagePath = string.Format(@"C:\Users\pf85ges\source\repos\Projet_POBJ_Reconaissance_Immage_V1\Projet_POBJ_Reconaissance_Immage_V1\images\baguette-1.jpg", AppDomain.CurrentDomain.BaseDirectory);
            Mat colorImage = Cv2.ImRead(imagePath, ImreadModes.Color);
            Mat blackNwhiteImage = Cv2.ImRead(imagePath, ImreadModes.Grayscale);

			colorImage.FindContours();

            Cv2.ImShow("BW Image", blackNwhiteImage);
            Cv2.WaitKey(0);

            
        }

		private void FindRectangles(Image<Gray, Byte> blackAndWhiteImage)
		{
			m_FoundRectangles.Clear();

			using (MemStorage storage = new MemStorage()) //allocate storage for contour approximation
			{
				for (Contour<Point> contours = blackAndWhiteImage.FindContours(
					Emgu.CV.CvEnum.CHAIN_APPROX_METHOD.CV_CHAIN_APPROX_SIMPLE,
					Emgu.CV.CvEnum.RETR_TYPE.CV_RETR_LIST,
					storage);
					contours != null;
					contours = contours.HNext)
				{
					Contour<Point> currentContour = contours.ApproxPoly(contours.Perimeter * 0.05, storage);
					//Debug.WriteLine(currentContour.Area);

					if (currentContour.Area > 250) //only consider contours with area greater than 250
					{
						if (currentContour.Total == 4) //The contour has 4 vertices.
						{
							if (IsRectangle(currentContour))
							{
								m_FoundRectangles.Add(currentContour.GetMinAreaRect());
							}
						}
					}
				}
			}
		}
	}
}
