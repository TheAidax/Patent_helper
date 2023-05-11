using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using US_Patent_Helper.Models;

namespace US_Patent_Helper.Data;

public class ApplicationDbContext : IdentityDbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }
    public DbSet<US_Patent_Helper.Models.RubberDuckies> RubberDuckies { get; set; } = default!;
}

