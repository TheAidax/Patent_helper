using System;
using IronPython.Hosting;
using IronPython.Runtime;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;
namespace US_Patent_Helper
{
	public class ImportedCompare
	{

        


        public ImportedCompare()
		{
            new PythonTuple(new[] { 1, 2, 3 }); // Use to construct python tuple in csharp

            var engine = Python.CreateEngine();

            var searchPaths = engine.GetSearchPaths();
            searchPaths.Add(@"path");
            engine.SetSearchPaths(searchPaths);

            var scope = engine.CreateScope();
            scope.SetVariable("x", 10);

            //var source = engine.CreateScriptSourceFromString(script, SourceCodeKind.Statements);
            var source = engine.CreateScriptSourceFromFile(@"path");

            var compilation = source.Compile();
            var result = compilation.Execute(scope);
            foreach (var varName in scope.GetVariableNames())
            {
                Console.WriteLine($"Variable: {varName}, Value: {scope.GetVariable(varName)}");

               

         
               

            }
        }
	}
}




