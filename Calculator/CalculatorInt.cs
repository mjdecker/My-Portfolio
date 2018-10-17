using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculator
{
    public class CalculatorInt      
    {
        //private data
        
        private int result;


        //properties for the client to interact with. These are the only public qualities to the class
        public string Input
        {
            set
            {
                this.result = evaluate(toPostfix(toInfix(value)));
            }
        }
        public int Result
        {
            get
            {
                return this.result;
            }
        }

        //if the client does not want the value saved, or wants to save it themselves
        public int calculate(string input)
        {
            return evaluate(toPostfix(toInfix(input)));
        }
        //helper function that assigns numbers to represent order of precedence of operators
        //higher number represents high priority.
        //low number represents error
        private int precedence(string o)
        {
            if (o == "+" || o == "-")
                return 1;
            else if (o == "*" || o == "/" || o == "X")
                return 2;
            else if (o == "^")
                return 3;
            else
                return -1;
        }

        //converts the input to an infix. Called every time that input is updated
        //assumes that input is formatted properly
        //Other methods do the hard work of formatting input
        //Proper format :
        //### + ### - ### etc.
        //All numbers are separated with a space, and all operators have a space on each side. 
        private List<string> toInfix(string input)     
        {
            List<string> infix = new List<string>();
            string temp = "";
            foreach (char c in input)
            {
                if (c == ' ')
                {
                    infix.Add(temp);
                    temp = "";
                }
                else if (c == 'X')
                {
                    temp += '*';
                }
                else
                {
                    temp += c;
                }
            }

            return infix;
        }

        //converts infix to postfix.
        private List<string> toPostfix(List<string> infix)
        {
            List<string> postfix = new List<string>();   
            Stack<string> operators = new Stack<string>();

            foreach (string s in infix)
            {
                if (Char.IsNumber(s[0])) //tests if string is a number
                {
                    postfix.Add(s);
                }
                else if (s == "(")
                {
                    operators.Push(s);
                }
                else if (s == ")")
                {
                    while (operators.Peek() != "(")
                        postfix.Add(operators.Pop());
                    operators.Pop();    //removes the "("

                }
                else    //if s is operator. Assumes valid input
                {       

                    //if operator is of proper precedence to merit popping operators from stack
                    while(operators.Count > 0 && operators.Peek() != "(" 
                        && precedence(s) <= precedence(operators.Peek())) 
                    {
                        postfix.Add(operators.Pop());
                    }
                    //operator gets added to stack
                    operators.Push(s);
                }


            }


            //cleaning off stack after all of infix has been processed
            while(operators.Count > 0)
                postfix.Add(operators.Pop());


            return postfix;
        }


        private int evaluate(List<string> postfix)
        {
            int result = 0; //not using the class data member until end of function

            Stack<int> operands = new Stack<int>();
            int operand1 = 0;
            int operand2 = 0;


            foreach(string s in postfix)
            {
                if (!Char.IsNumber(s[0]))   //if s is an operator
                {
                    operand2 = operands.Pop();
                    operand1 = operands.Pop();

                    switch (s[0])
                    {
                        case '+':
                            operands.Push(checked(operand1 + operand2));
                            break;
                        case '-':
                            operands.Push(checked(operand1 - operand2));
                            break;
                        case '*':
                            operands.Push(checked(operand1 * operand2));
                            break;
                        case '/':
                            if (operand2 == 0)
                                throw new DivideByZeroException("Divide by zero Error");
                            else
                                operands.Push(checked(operand1 / operand2));
                            break;
                        case '^':
                            throw new NotImplementedException("The ^ operation is not yet supported");
                            break;
                        default:
                            throw new ArithmeticException("Attempted to operate on something which is not an operator!");
                            break;
                    }

                }
                else
                {
                    int temp = 0;
                    Int32.TryParse(s, out temp);
                    operands.Push(temp);
                }             

            }



            if (operands.Count != 1)
                throw new Exception("Something weird happened, look at evaluate method to debug.");
            else
                return operands.Pop();

        }



    }
}
