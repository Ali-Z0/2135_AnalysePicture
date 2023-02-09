//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using Emgu.CV;
//using Emgu.CV.Structure;
//using System.Drawing;
//using System.Diagnostics;
//using Vision;

//namespace CameraCalibrator
//{
//	internal class MainFormModel
//	{
//		private Capture m_Capture;
//		private Rectangle m_RegionOfInterest = new Rectangle(33, 100, 270, 120);

//		private Image<Bgr, Byte> m_OriginalImage = null;
//		private Image<Bgr, Byte> m_ClippedImage = null;
//		private Image<Bgr, Byte> m_ErodedImage = null;
//		private Image<Gray, Byte> m_GrayImage = null;
//		private Image<Gray, Byte> m_BlackAndWhiteImage = null;
//		private Image<Bgr, Byte> m_FoundRectanglesImage = null;

//		private CalibrationImage m_ImageModel = new CalibrationImage(7, 3, 30, 75);
//		private List<MCvBox2D> m_FoundRectangles = new List<MCvBox2D>();
//		private int m_FoundRectangleCount;

//		public event EventHandler Changed;

//		public MainFormModel()
//		{
//			m_Capture = new Capture();
//			m_Capture.FlipHorizontal = true;
//			m_Capture.FlipVertical = true;
//		}

//		public Rectangle RegionOfInterest
//		{
//			get { return m_RegionOfInterest; }
//			set { m_RegionOfInterest = value; }
//		}

//		public void ProcessFrame(int threshold)
//		{
//			m_OriginalImage = m_Capture.QueryFrame();

//			m_ClippedImage = m_OriginalImage.Copy(this.RegionOfInterest);

//			// Make the dark portions bigger
//			m_ErodedImage = m_ClippedImage.Erode(1);

//			//Convert the image to grayscale
//			m_GrayImage = m_ErodedImage.Convert<Gray, Byte>();

//			m_BlackAndWhiteImage = m_GrayImage.ThresholdBinaryInv(new Gray(threshold), new Gray(255));

//			FindRectangles(m_BlackAndWhiteImage);

//			this.FoundRectangleCount = m_FoundRectangles.Count;
//			if (this.FoundRectangleCount == m_ImageModel.ExpectedRectangleCount)
//			{
//				m_ImageModel.AssignFoundRectangles(m_FoundRectangles);
//				m_FoundRectanglesImage = CreateRectanglesImage(m_ImageModel.GetInsideRectangles());
//			}
//			else
//			{
//				m_FoundRectanglesImage = CreateRectanglesImage(m_FoundRectangles);
//			}
//		}

//		private void FindRectangles(Image<Gray, Byte> blackAndWhiteImage)
//		{
//			m_FoundRectangles.Clear();

//			using (MemStorage storage = new MemStorage()) //allocate storage for contour approximation
//			{
//				for (Contour<Point> contours = blackAndWhiteImage.FindContours(
//					Emgu.CV.CvEnum.CHAIN_APPROX_METHOD.CV_CHAIN_APPROX_SIMPLE,
//					Emgu.CV.CvEnum.RETR_TYPE.CV_RETR_LIST,
//					storage);
//					contours != null;
//					contours = contours.HNext)
//				{
//					Contour<Point> currentContour = contours.ApproxPoly(contours.Perimeter * 0.05, storage);
//					//Debug.WriteLine(currentContour.Area);

//					if (currentContour.Area > 250) //only consider contours with area greater than 250
//					{
//						if (currentContour.Total == 4) //The contour has 4 vertices.
//						{
//							if (IsRectangle(currentContour))
//							{
//								m_FoundRectangles.Add(currentContour.GetMinAreaRect());
//							}
//						}
//					}
//				}
//			}
//		}

//		/// <summary>
//		/// Determines whether the angles are close enough to 90 degrees
//		/// </summary>
//		/// <param name="contour"></param>
//		/// <returns></returns>
//		private bool IsRectangle(Contour<Point> contour)
//		{
//			Point[] pts = contour.ToArray();
//			LineSegment2D[] edges = PointCollection.PolyLine(pts, true);

//			for (int i = 0; i < edges.Length; i++)
//			{
//				LineSegment2D currentEdge = edges[i];
//				LineSegment2D nextEdge = edges[(i + 1) % edges.Length];

//				double angle = Math.Abs(nextEdge.GetExteriorAngleDegree(currentEdge));
//				if (angle < 80 || angle > 100)
//				{
//					return false;
//				}
//			}

//			return true;
//		}

//		private Image<Bgr, Byte> CreateRectanglesImage(IEnumerable<MCvBox2D> rectangles)
//		{
//			Image<Bgr, Byte> rectangleImage = m_ClippedImage.CopyBlank();
//			int width = 0;
//			foreach (MCvBox2D box in rectangles)
//			{
//				MCvBox2D box1 = new MCvBox2D(
//					box.center,
//					new SizeF(2, 2),
//					0);
//				width++;
//				//Debug.WriteLine(width);
//				rectangleImage.Draw(box1, new Bgr(Color.White), width);
//			}
//			return rectangleImage;
//		}

//		public Image<Bgr, Byte> OriginalImage
//		{
//			get { return m_OriginalImage; }
//		}

//		public Image<Bgr, Byte> ClippedImage
//		{
//			get { return m_ClippedImage; }
//		}

//		public Image<Bgr, Byte> ErodedImage
//		{
//			get { return m_ErodedImage; }
//		}

//		public Image<Gray, Byte> GrayImage
//		{
//			get { return m_GrayImage; }
//		}

//		public Image<Gray, Byte> BlackAndWhiteImage
//		{
//			get { return m_BlackAndWhiteImage; }
//		}

//		public Image<Bgr, Byte> FoundRectanglesImage
//		{
//			get { return m_FoundRectanglesImage; }
//		}

//		public int ExpectedRectangleCount
//		{
//			get { return m_ImageModel.ExpectedRectangleCount; }
//		}

//		public int FoundRectangleCount
//		{
//			get { return m_FoundRectangleCount; }
//			private set
//			{
//				if (value == m_FoundRectangleCount)
//				{
//					return;
//				}
//				m_FoundRectangleCount = value;
//				RaiseChangedEvent();
//			}
//		}

//		public bool CaptureIsPossible
//		{
//			get { return this.FoundRectangleCount == this.ExpectedRectangleCount; }
//		}

//		public void CaptureCalibration()
//		{
//			Debug.Assert(CaptureIsPossible);
//			CameraVsPhysicalPoint[,] cameraVsPhysicalPoints = m_ImageModel.GetCameraVsPhysicalPoints();
//			//Print(cameraVsPhysicalPoints);

//			Vision.CameraCalibration.Instance.Initialize(cameraVsPhysicalPoints);
//		}

//		private void Print(CameraVsPhysicalPoint[,] cameraVsPhysicalPoints)
//		{
//			int xCount = cameraVsPhysicalPoints.GetLength(0);
//			int yCount = cameraVsPhysicalPoints.GetLength(1);

//			Debug.WriteLine("---- cameraVsPhysicalPoints ----");
//			for (int i = 0; i < xCount; i++)
//			{
//				for (int j = 0; j < yCount; j++)
//				{
//					CameraVsPhysicalPoint point = cameraVsPhysicalPoints[i, j];
//					string line = String.Format(
//						"{0},{1}   {2:###},{3:###}   {4:###},{5:###}",
//						i, j, point.PhysicalPoint.X, point.PhysicalPoint.Y, point.CameraPoint.X, point.CameraPoint.Y);
//					Debug.WriteLine(line);
//				}
//			}
//		}

//		private void RaiseChangedEvent()
//		{
//			EventHandler handler = this.Changed;
//			if (handler != null)
//			{
//				handler(this, EventArgs.Empty);
//			}
//		}
//	}
//}