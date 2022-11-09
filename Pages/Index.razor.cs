using System.Text.Json;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Components;

namespace BlazorPage.Pages {
    public partial class Index : ComponentBase {
            [Inject]
            protected HttpClient Client {get; set;} = null!;
            protected Root? Root {get;set;}

            protected override async Task OnParametersSetAsync() {
                Root = await Client.GetFromJsonAsync<Root>("ContentsMap.json");
                Console.WriteLine(JsonSerializer.Serialize<Root>(Root));
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