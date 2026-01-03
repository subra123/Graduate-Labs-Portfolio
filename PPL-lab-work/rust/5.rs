#[derive(Clone)]

struct BankAcc{
    no:String,
    name: String,
    bal: i32
}

impl BankAcc{
    fn new(no: &str,name: &str, bal: i32)-> Self{
        Self
        {   
           no: no.to_string(),
           name:name.to_string(),
            bal:bal,
        }
    }
    fn view_bal(&self){
        println!("the bal is {}" , self.bal);
    }
    fn deposit(&mut self, amt:i32){
        self.bal += amt;
    }

    fn withdraw(&mut self, amt:i32){
        self.bal -= amt;
    }
}

fn main(){
    let mut acc1 = BankAcc::new("1234","subu",1000);
    acc1.view_bal();
    acc1.deposit(100);
    
    acc1.view_bal();
    acc1.withdraw(200);
    acc1.view_bal();
}
