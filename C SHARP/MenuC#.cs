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

        public static int fatorial(int n)
        {

            if ((n == 1) || (n == 0)) return 1;
            else
                return fatorial(n - 1) * n;
        }










        public static void tabuada(int numero)
        {

            Console.WriteLine("==================================================");
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(numero + "X" + i + "=" + numero * i);

            }
            Console.WriteLine("==================================================");
        }

        private static void calcularMedia()
        {
            int qtdnotas = 3;
            List<int> notas = new List<int>();
            double media = 0;
            for (int i = 0; i < qtdnotas; i++) {

                Console.WriteLine("Insira a nota de numero : " + i);
                int valor = Convert.ToInt32(Console.ReadLine());
                notas.Add(valor);

                media = notas[i] + media;


            }
            Console.WriteLine("A Média das provas foi : {0:F2}", media / 3);








        }









        private static void lerArquivo(int numeroDoArquivo)
        {

            string caminhoDoArquivo = @"C:\Users\user\Documents\arquivos\arq" + numeroDoArquivo + ".txt";
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

        public static void menuOpcoes(){


            while (true)
            {
                string mensagem = "Olá,para usar o menu DIGITE : " + "\n" + "\n   0- PARA SAIR" + "\n    1- PARA LER ARQUIVOS" + "\n     2- CALCULAR MEDIA" + "\n      3- TABUADA" + "\n       4- FATORIAL" + "\n";
                Console.WriteLine("==================================================");
                Console.WriteLine(mensagem);
                Console.WriteLine("==================================================");

               
                int option = Convert.ToInt32(Console.ReadLine());


                if (option == SAIDA_PROGRAMA)
                {
                    Console.WriteLine("bye :(");
                    break;
                }
                else
                { }
                if (option == LER_ARQUIVOS)
                {
                    lerArquivo(1);
                }
                else
                {
                }
                if (option == CALCULAR_MEDIA)
                {
                    calcularMedia();
                }
                else
                {



                }
                if (option == TABUADA)
                {
                    Console.WriteLine("Insira o valor para a tabuada");
                    int z = Convert.ToInt32(Console.ReadLine());
                    tabuada(z);
                }
                else
                {


                }
                if (option == FATORIAL)
                {
                    Console.WriteLine("Insira o numero que quer saber o fatorial ");
                    int fat = Convert.ToInt32(Console.ReadLine());

                    int valorf = 0;
                    valorf = fatorial(fat);
                    Console.WriteLine(valorf);

                }
                else
                {

                    Console.WriteLine("Opcao Invalida");
                }



            }


        }

        public const int SAIDA_PROGRAMA = 0;
        public const int LER_ARQUIVOS = 1;
        public const int CALCULAR_MEDIA = 2;
        public const int TABUADA = 3;
        public const int FATORIAL = 4;
        static void Main(string[] args)
        {

            menuOpcoes();       

            
        }
    }
}

