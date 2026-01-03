#[derive(Clone)]
struct Lib{
   title:String,
   isbn: String,
   author: String,
   is_issued: bool 
}

impl Lib {
    fn new(title: &str,author: &str,isbn: &str) -> Self{
        Self{
    title: title.to_string(),
    isbn: isbn.to_string(),
    author: author.to_string(),
    is_issued:false 
        }
    }
    fn issued(&mut self){
        self.is_issued =true;
    }
}

fn main(){
    let mut book = Lib::new("50 shades of grey","69","hm");
    let lib_backup = book.clone();

    println!("Book Info ");
    println!("Book Title:{} \nBook isbn:{} \nBook Author:{}", lib_backup.title , lib_backup.isbn ,lib_backup.author )
}
