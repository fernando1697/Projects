using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp6
{
    class Program
    {
private static void lerArquivo(int numeroDoArquivo)
        {

            string caminhoDoArquivo = @"C:\Users\user\Documents\arquivos\arq"+numeroDoArquivo+".txt";
            if (File.Exists(caminhoDoArquivo))
            {

                using (StreamReader arquivo = File.OpenText(caminhoDoArquivo))
                {
                    string linha;
                    while ((linha = arquivo.ReadLine()) != null)
                    {
                        Console.WriteLine(linha);
                    }
                }
            
            

                String caminhoDoArquivo2 = @"C:\Users\user\Documents\arquivos\arq" + (numeroDoArquivo + 1) + ".txt";

                if (File.Exists(caminhoDoArquivo2))
                {

                    lerArquivo(numeroDoArquivo + 1);
                }
            }
        }


        

        static void Main(string[] args)
        {

            lerArquivo(1);
            
        }
    }
}

