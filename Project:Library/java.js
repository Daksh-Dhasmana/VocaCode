const forms=document.getElementById("libform");
const dialog=document.getElementById("libr");
const disph=document.getElementById("disph");
const showbtn=document.getElementById("showform");
showbtn.addEventListener("click",()=>{
    dialog.showModal();
})
const lib=[];//An array to store books
function conbook(aname,bname, page){//constructor
    this.page=page;
    this.id=crypto.randomUUID();
    this.bname=bname;
    this.aname=aname;
}
const addBook=(aname,bname,page)=>{// Create book then store it in array
    const newbook=new conbook(bname,aname,page);
    lib.push(newbook);
}
const dispbook=()=>{//Displays Books
    const dip=document.getElementById("display");
    dip.innerHTML=" ";
    if(lib.length===0){div.innerHTML="Empty Library"};
    for (let i = 0; i < lib.length; i++) {
        const div=document.createElement('div');
        div.innerHTML+=`${lib[i].bname} by ${lib[i].aname} contains ${lib[i].page} pages`
        dip.appendChild(div);
    }
}
disph.addEventListener('click',(e)=>{
    dispbook();
})
forms.addEventListener('submit',(e)=>{//gets details from forms and adds them to list
    e.preventDefault();
    const aname=document.getElementById("aname").value;
    const bname=document.getElementById("bname").value;
    const page=document.getElementById("npage").value;
    addBook(aname,bname,page);
    dialog.close();
})
