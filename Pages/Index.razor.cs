using System.Text.Json;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Components;

namespace BlazorPage.Pages {
    public partial class Index : ComponentBase {
            [Inject]
            protected HttpClient Client {get; set;} = null!;
            protected Root? Contents {get;set;}

            protected override async Task OnParametersSetAsync() {
                var root = await Client.GetFromJsonAsync<Root>("ContentsMap.json");
                Contents = root.Children.Where(item => item.Name == "posts").FirstOrDefault();
                Console.WriteLine(JsonSerializer.Serialize<Root>(root));
            }
    }

    public class Root {
            public string? Name { get; set; }
            public string? Path { get; set; }
            public string? Extention { get; set; }
            public string? Type { get; set; }
            public List<Root>? Children { get; set; }
    }
}