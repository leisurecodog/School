class Check{
    constructor()
    {
      this.CK=this.CK.bind(this);
      document.querySelector('.LogButton').addEventListener('click',this.CK);
      document.querySelector('img').addEventListener('click',this.back);
    }
    CK()
    {
      //alert(escape("1S3:5?7"));
      const con=document.querySelectorAll('.input');
      for(var x in USER)
      {
        if(USER[con[0].value]==con[1].value)
        {
          alert("success");
          document.location.href="index.html?"+con[0].value;
        }
        else {
          alert("fail");
        }
      }
    }
    back()
    {
      document.location.href='index.html';
    }
}


const ck= new Check;
const USER=
  {
    'admin':'admin'
  };
