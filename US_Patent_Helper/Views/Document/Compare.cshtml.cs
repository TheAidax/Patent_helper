using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace US_Patent_Helper.Views.Document
{
	public class CompareModel : PageModel
    {
        public void OnGet()
        {
        }

        public void OnClick()
        {
            Console.WriteLine("Button Clicked");
     
        }
    }
}
