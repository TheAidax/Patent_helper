using System;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore.Metadata.Internal;
using System.Diagnostics;
using US_Patent_Helper.Models;
using System.Linq;
using System.Web;
using Azure.Core;
using static Community.CsharpSqlite.Sqlite3;
using static IronPython.Modules._ast;


namespace US_Patent_Helper.Controllers
{
	public class DocumentController :Controller
	{
        private readonly Microsoft.AspNetCore.Hosting.IHostingEnvironment _hostingEnvironment;
        [HttpGet]
		public ActionResult Document()
		{
            return View();
        }

        public ActionResult Compare()
        {
            return View();
        }


        [HttpPost]
        public ActionResult UploadDocument(IFormFile postedFile)
		{
            string contentRootPath = _hostingEnvironment.ContentRootPath;
            string webRootPath = _hostingEnvironment.WebRootPath;

            String filePath = "";
			//filePath = MapPath("~/Files/");
            filePath = Path.Combine(_hostingEnvironment.ContentRootPath, "~/Files/");
            if (postedFile == null)
            {
				postedFile = Request.Form.Files["documentFile"];
            }

            if (!Directory.Exists(filePath))
			{
				Directory.CreateDirectory(filePath);

			}
			filePath = filePath + Path.GetFileName(postedFile.FileName);
			//postedFile.SaveAs(filePath);
			ViewBag.Message = "File Saved";

			return View();

		}

		public DocumentController(Microsoft.AspNetCore.Hosting.IHostingEnvironment hostingEnvironment)
		{
            _hostingEnvironment = hostingEnvironment;
        }
		
    }
}

