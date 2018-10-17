using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Calculator;

namespace CalculatorProgram
{
    public partial class frmCalculator : Form
    {
        //data needed
        private CalculatorInt calculator;


        public frmCalculator()
        {
            InitializeComponent();
        }


        //helper methods
        private void NumBtnPushed(int n)
        {
            int temp = 0;

            //ensuring that parse will be successful
            if (txtOutput.Text != "Integer Overflow!")
                Int32.TryParse(txtOutput.Text, out temp);

            
            if (txtOutput.Text != "0" && temp < Int32.MaxValue - 10)
                txtOutput.Text += n.ToString();
            else if (temp > Int32.MaxValue - 10)
                txtOutput.Text = "Integer Overflow!";
            else
                txtOutput.Text = n.ToString();
        }

        //initializes the calculator class.
        private void frmCalculator_Load(object sender, EventArgs e)
        {
            calculator = new CalculatorInt();
        }

        /*
         * These event handlers handle the pushing of the number buttons and simply
         * call the helper method NumBtnPushed()
         */
        private void btn1_Click(object sender, EventArgs e)
        {
            NumBtnPushed(1);
        }
        private void btn2_Click(object sender, EventArgs e)
        {
            NumBtnPushed(2);
        }
        private void btn3_Click(object sender, EventArgs e)
        {
            NumBtnPushed(3);
        }
        private void btn4_Click(object sender, EventArgs e)
        {
            NumBtnPushed(4);
        }
        private void btn5_Click(object sender, EventArgs e)
        {
            NumBtnPushed(5);
        }
        private void btn6_Click(object sender, EventArgs e)
        {
            NumBtnPushed(6);
        }
        private void btn7_Click(object sender, EventArgs e)
        {
            NumBtnPushed(7);
        }
        private void btn8_Click(object sender, EventArgs e)
        {
            NumBtnPushed(8);
        }
        private void btn9_Click(object sender, EventArgs e)
        {
            NumBtnPushed(9);
        }
        private void btn0_Click(object sender, EventArgs e)
        {
            NumBtnPushed(0);
        }




    }
}
