using System;
using System.ComponentModel.DataAnnotations;

namespace US_Patent_Helper.Models
{
	public class Document
	{
		public string UserID { get; set; }
		public int ID { get; set; }
		public string? name { get; set; }
        [DataType(DataType.Upload)]
        public HttpPostedFileBase ImageUpload { get; set; }

        public Document()
		{
		}
	}
}

