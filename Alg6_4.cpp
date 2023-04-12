#include<iostream>
#include<vector>

using std::cout;
using std::cin;
using std::vector;

int N, M;


vector<int> visited;
vector<int> value;
vector<int> cycle;

int dfs(vector<vector<int>> graph, int now)
{
    if(visited[now] != 2)
    {
        visited[now] = 1;

            for(int i = 0; i < size(graph[now]); i++)
            {
                int neig = graph[now][i];

                if(visited[neig] == 0)
                {
                    if(!dfs(graph, neig)) return 0;
                    int count = 0;
                    for(int j = 0; j < size(value); j++)
                    {
                        if(value[j] == neig)
                        {
                            count++;
                        }
                    }
                    if(count == 0)
                    {
                        value.push_back(neig);
                    }
                    else count = 0;
                }
                else if(visited[neig] == 1) return 0;
                else continue;
                visited[neig] = 2;
            }

            int count = 0;
            for(int j = 0; j < size(value); j++)
            {
                if(value[j] == now)
                {
                    count++;
                }
            }
            if(count == 0)
            {
                value.push_back(now);
            }
            else count = 0;
            visited[now] = 2;
            return 1;
    }
    else if (visited[now] == 1) return 0;
    else return 1;
    
}

int main()
{

    cin >> N >> M;
    vector<vector<int>> graph(N + 1);
    for(int i = 1; i < M + 1; i++)
    {
        int value_1, value_2;
        cin >> value_1 >> value_2;
        graph[value_1].push_back(value_2);
    }
    visited.resize(N + 1);
    int count = 0;

    for(int i = 1; i < N + 1; i++)
    {
        if(!dfs(graph, i))
        {
            count++;
            break;
        }
    }

    if(count == 0)
    {
        for(int i = (size(value) - 1); i >= 0; i--)
        {
            cout << value[i] << " ";
        }
    }
    else cout << -1;
}
