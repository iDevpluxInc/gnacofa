//events and news functions

//document.addEventListener('contextmenu',event => event.preventDefault());

// FUNCTION FOR ID DISPLAY BOX
function changeStatus(){
  var status = document.getElementById("id");
  if (status){
    document.getElementById("idNum").style.display="block";
  }
  else{
    document.getElementById("idNum").style.display="none";
  }
}

//function for married
function marriageStatus(){
  var status1 = document.getElementById("marriage");
  if (status1.value =="Married"){
    document.getElementById("spouseDetails").style.display="block";
  }
  else{
    document.getElementById("spouseDetails").style.display="none";
  }
  if (status1.value == "Divorced") {
    document.getElementById("np").style.display="none"; 
  }
  else{
    document.getElementById("np").style.display="none"; 
  }
}


function selectStatus(){
    var status2=document.getElementById("NumFarm");
    if (status2.value == "One"){
      document.getElementById("opp").style.display="block";
    }
    else{
      document.getElementById("opp").style.display="none";
    }
    if(status2.value == "Two"){
      document.getElementById("ppo").style.display="block";
    }
    else{
      document.getElementById("ppo").style.display="none";
    }
    if(status2.value=="Three"){
      document.getElementById("pop").style.display="block";
    }
    else{
      document.getElementById("pop").style.display="none";
    }
    if(status2.value=="Four"){
      document.getElementById("ppp").style.display="block";
    }
    else{
      document.getElementById("ppp").style.display="none";
    }
    if(status2.value=="Five"){
      document.getElementById("pppo").style.display="block";
    }
    else{
      document.getElementById("pppo").style.display="none";
    }
  }



  // OPTION 1 //
function Ownership(){
    var status3=document.getElementById("farmOwner");
    if (status3.value == "Self"){
      document.getElementById("numlabour").style.display="block";
    }
    else{
      document.getElementById("numlabour").style.display="none";
    }
    if (status3.value == "Rented"){
      document.getElementById("durr").style.display="block";
    }
    else{
      document.getElementById("durr").style.display="none";
    }
    if (status3.value == "Labourer"){
      document.getElementById("labour").style.display="block";
    }
    else{
      document.getElementById("labour").style.display="none";
    }
    if (status3.value== "Crop Sharing (DV 2)"){
      document.getElementById("crDivision").style.display="block";
    }
    else{
      document.getElementById("crDivision").style.display="none";
    }
    if (status3.value == "Family"){
      document.getElementById("family").style.display="block";
    }
    else{
      document.getElementById("family").style.display="none";
    }         
  }
/* ***********************************END *********************/


// business selction area//
function Business(){
    var answer=document.getElementById("sideBusiness");
    if (answer.value == "Yes"){
      document.getElementById("sidebuss").style.display="block";
    }
    else{
      document.getElementById("sidebuss").style.display="none";
    }
  }
function currentBusiness(){
    var val=document.getElementById("currentBuss");
    if (val.value == "Yes"){
      document.getElementById("currentbuss").style.display="block";
    }
    else{
      document.getElementById("currentbuss").style.display="none";
    }
  }

function BankTransacting(){
    var bank=document.getElementById("questionBanks");
    if (bank.value == "Yes"){
      document.getElementById("bankTrans").style.display="block";
    }
    else{
      document.getElementById("bankTrans").style.display="none";
    }
  }
//                        END                             //

// Region selction  at this point//
  function select(){
    var district = document.getElementById("region")
    if(district.value == "Ashanti"){
      document.getElementById("ashanti").style.display="block";
    }
    else{
      document.getElementById("ashanti").style.display="none";
    }
    if(district.value == "Ahafo"){
      document.getElementById("ahafo").style.display="block";
    }
    else{
      document.getElementById("ahafo").style.display="none";
    }
    if(district.value == "Bono"){
      document.getElementById("bono").style.display="block";
    }
    else{
      document.getElementById("bono").style.display="none";
    }
    if(district.value == "Western"){
      document.getElementById("western").style.display="block";
    }
    else{
      document.getElementById("western").style.display="none";
    }
    if(district.value == "WesternNorth"){
      document.getElementById("westernnorth").style.display="block";
    }
    else{
      document.getElementById("westernnorth").style.display="none";
    }
    if(district.value == "Central"){
      document.getElementById("central").style.display="block";
    }
    else{
      document.getElementById("central").style.display="none";
    }
    if(district.value == "BonoEast"){
      document.getElementById("bonoeast").style.display="block";
    }
    else{
      document.getElementById("bonoeast").style.display="none";
    }
    if(district.value == "Oti"){
      document.getElementById("oti").style.display="block";
    }
    else{
      document.getElementById("oti").style.display="none";
    }
    if(district.value == "Volta"){
      document.getElementById("volta").style.display="block";
    }
    else{
      document.getElementById("volta").style.display="none";
    }
    if(district.value == "Eastern"){
      document.getElementById("eastern").style.display="block";
    }
    else{
      document.getElementById("eastern").style.display="none";
    }                      
  }

  // *************************** END OF REGION SELECTION *************//

function events(){
      var events=document.getElementById("evebutts");
      if (events.value == "evebutt"){
        document.getElementById("bankTrans").style.display="block";
      }
      else{
        document.getElementById("bankTrans").style.display="none";
      }
}

//COMMENT FOR  EVENTS AND NEWS SHOW AND HIDDEN FEATURES //
function changee(){
  var chang = document.getElementById("evet");
  if(chang){
    document.getElementById("events").style.display = "block";
  }
  else{
    document.getElementById("events").style.display ="none";
  }
}

function change(){
  var chan = document.getElementById("new");
  if(chan){
    document.getElementById("news").style.display = "block";
  }
  else{
    document.getElementById("news").style.display ="none";
  }
}
// farm details //

$(document).ready(function(){
  $(".add_item_btn").click(function(e){
    e.preventDefault();
    $("#show_item").prepend(`<div id="show_item">
              <div class="flex flex-row">
                <div class="col">
                  <label for="ownerOfFarm">Owner of Farm *</label>
                  <select class="form-select" id="farmOwner"  onChange="Ownership()" name="farmOwner1">
                    <option selected style="font-style: italic; font-family: poppin;">Select Farm Owner</option>
                    <option value="Self">SELF</option>
                    <option value="Labourer">Labourer</option>
                    <option value="Rented">Rented/Lease</option>
                    <option value="Crop Sharing (DV 2)">Crop Sharing (DV 2)</option>
                    <option value="Family">Family</option>                                             
                  </select>
                </div>

                <div class="col" id="durr" style="display: none;">
                  <label for="nlabourers">Number of labourers *</label>
                  <input type="number" class="form-control" name="nlabourers" id="nlabourers" placeholder="Enter Number of labourers"/>
                </div>
                <div class="col" id="durr" style="display: none;">
                  <label for="duration">Duration *</label>
                  <input type="number" class="form-control" name="duration" id="duration" placeholder="Enter How long"/>
                </div>
                <div class="col" id="labour" style="display: none;">
                  <label for="duration">Name of Owner *</label>
                  <input class="form-control" type="text" name="ownerName" id="ownerName" placeholder="Enter the Owner's Name"/>
                    <br>
                  <label for="ownerGFX">Owners GFX</label>
                  <input class="form-control" typ="number" name="ownerGFX" id="ownerGFX" placeholder="Enter the Owner's GFX Number if any."/>
                </div>
                <div class="col" id="crDivision" style="display: none;">
                  <label for="personsInvolved"> How many people *</label>
                  <input type="number" class="form-control" name="numPeople" id="numPeople" placeholder="Enter number of People"/>
                </div>

                <div class="col" id="family" style="display: none;">
                  <label for="personsInvolved"> Names of family *</label>
                  <input type="text" class="form-control" name="familyPeople[]" id="familyPeople" placeholder="Enter number of People"/>
                </div>

                <div class="col">
                  <label for="cropCultivated">Crop Cultivated</label>
                  <input class="form-control" type="text"  value="Cocoa" name="cropcultivated" id="cropcultivated" placeholder="Crop Cultivated"/>
                </div>
                <div class="col">
                  <label for="farmSize">Farm Size *</label>
                  <input class="form-control" type="number"  name="farmSize" id="farmSize" placeholder="Farm Size"/>
                </div>
                <div class="col">
                  <label for="farmLocation">Farm Location *</label>
                  <input class="form-control" type="text"  name="farmLocation" id="farmLocation" placeholder="Farm Size"/>
                </div>
                <div class="col">
                  <br>
                  <input type="button" value="Remove Added Field" class="p-2 bg-red-500 hover:bg-red-800 remove_item_btn">
                </div>
              </div>
            </div>`);
  });
  $(document).on('click', '.remove_item_btn',function(e){
    e.preventDefault();
    let row_item = $(this).parent().parent();
    $(row_item).remove();
  });
});



  // UNKOWN SOURCE COPIED FROM ONLINE BUT VERY USFULLY CODES BELOW//
  //  this code is for Tables control//
    $(document).ready(function () {
      $('#data').DataTable({
        "scrollX": true,
        "orderable": false,
        "searchable":true,    
      });
    });
  
$(document).ready(function(){

  $('[data-toggle="popover"]').popover();

});



// this code is for carousel -----------HomePage-----------//
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

