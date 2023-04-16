using System;
using IronPython.Hosting;


public class ImportPythonData
{

    public int ImportData()
    {
        // new PythonTuple(new[] { 1, 2, 3 }); // Use to construct python tuple in csharp


/*
        var engine = Python.CreateEngine();

        var searchPaths = engine.GetSearchPaths();
        searchPaths.Add(@"path");
        engine.SetSearchPaths(searchPaths);
*/
        var scope = engine.CreateScope();
        // scope.SetVariable("x", 10);

        //var source = engine.CreateScriptSourceFromString(script, SourceCodeKind.Statements);
        var source = engine.CreateScriptSourceFromFile(@"tuple_test.py");
        var source2 = engine.CreateScriptSourceFromFile(@"standard_test.py");

        var compilation = source.Compile();
        var result = compilation.Execute(scope);

        /* foreach (var varName in scope.GetVariableNames())
        {
            Console.WriteLine($"Variable: {varName}, Value: {scope.GetVariable(varName)}");






        }
        */

        Console.WriteLine("Directly from python program: \n:" + $"Variable: {scope.GetVariable("generateList")}");

        var listOfTuples = scope.GetVariable("generateList");

        Console.WriteLine("List of tuples stored in C# but acquired from python: \n" + listOfTuples);


        return 0;
    }
}


