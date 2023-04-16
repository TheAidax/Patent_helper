using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using US_Patent_Helper.Models;
using System.Linq;
using System.Web;
using Microsoft.AspNetCore.Authorization;
namespace US_Patent_Helper.Controllers;



public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;

    public HomeController(ILogger<HomeController> logger)
    {
        _logger = logger;
    }

    [Authorize]
    public IActionResult Index()
    {
       /* String path = Server.MapPath("~/images/");
        String[] imagesfiles = Directory.GetFiles(path);
        ViewBag.images = imagesfiles; 

             @foreach(var file in ViewBag.images)
{ 
                <img src ="~/images/@Path.GetFileName(file)"/>
} */

        /* 
         * Giannis
         * Middleton
         * Lopez
         * Matthews
         * Holiday
         * Thanansis
         * Connington
         * Portis
         * WHite boy from Utah
         * Jevon Carter
         * Shooter w dreads that played for the CEltics a few years ago
         * Greyson Allen
         */

        return View();
    }

    public IActionResult About()
    {
        return View();
    }

    [Authorize]
    public IActionResult ViewDocument()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}

