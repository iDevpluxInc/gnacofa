
//function for farm selection
// form one
function ownerShip(){
  var obj = document.getElementById("Owner");
  if (obj.value =="Self"){
    document.getElementById("forself").style.display="block";
  }else{
    document.getElementById("forself").style.display="none";
  }
  if (obj.value == "Labour"){
    document.getElementById("labour").style.display="block";
  } else {
    document.getElementById("labour").style.display="none";
  }

  if (obj.value == "Rented"){
    document.getElementById("rented").style.display="block";
  } else {
    document.getElementById("rented").style.display="none";
  }

  if (obj.value == "CropSharing"){
    document.getElementById("cropsharing").style.display="block";
  } else {
    document.getElementById("cropsharing").style.display="none";
  }
  if (obj.value == "Family"){
    document.getElementById("family").style.display="block";
  } else {
    document.getElementById("family").style.display="none";
  }
}




/// for  form validators ///
function showError(errorElement, errorMessage){
    document.querySelector("."+errorElement).classList.add("display-error");
    document.querySelector("."+errorElement).innerHTML=errorMessage;
}
function clearError(){
    let errors =document.querySelectorAll(".error");

    for(let error of errors){
        error.classList.remove("display-error");
    }
}
let form = document.forms['add-member-form'];
form.onsubmit = function(){
    clearError();

    if (form.gfx.value === ""){
        showError("gfx-error", "you've got to Enter a gfx number here");
        return false;
    }
    if (form.region.value === "Please Select Region"){
        showError("region-error", "Please select a region");
        return false;
    }
    if (form.district.value === "Please Select district"){
        showError("district-error", "Please select a district");
        return false;
    }
    if (form.society.value === ""){
        showError("society-error", "please Enter member's society");
        return false;
    }
    if (form.title.value === "Please Select title"){
        showError("title-error", "please select a title");
        return false;
    }
    if (form.image.value === ""){
        showError("image-error", "please click to upload image this member");
        return false;
    }
    if (form.first_name.value === ""){
        showError("first_name-error", "please input first name...");
        return false;
    }
    if (form.last_name.value === ""){
        showError("last_name-error", "please input last name....");
        return false;
    }
    if (form.gender.value === "Please Select Gender"){
        showError("gender-error", "please select Gender");
        return false;
    }
    if (form.society.value === ""){
        showError("society-error", "please Enter member's society");
        return false;
    }

    if (form.day.value === ""){
        showError("day-error", "please Enter Day of birth");
        return false;
    }

    if (form.month.value === "Please Select month"){
        showError("month-error", "please Enter Month of birth");
        return false;
    }

    if (form.year.value === ""){
        showError("year-error", "please Enter Year of birth");
        return false;
    }
    if (form.hometown.value === ""){
        showError("hometown-error", "Hometown Required!!!!");
        return false;
    }

    if (form.address.value === ""){
        showError("address-error", "Address Required!!!!");
        return false;
    }
    if (form.loe.value === ""){
        showError("loe-error", "Level of Education Required!!!!");
        return false;
    }
    if (form.idtype.value === "Please Select ID type"){
        showError("idtype-error", "Type of ID Required!!!!");
        return false;
    }
    if (form.idnum.value === ""){
        showError("idnum-error", "Id Number Required!!!!");
        return false;
    }
    if (form.phone.value === ""){
        showError("phone-error", "Phone Number Required!!!!");
        return false;
    }
    if (form.mstatus.value === "Please select status"){
        showError("mstatus-error", "Marital Status Required!!!!");
        return false;
    }
    if (form.kinfullname.value === ""){
        showError("kinfullname-error", "Next of kin's Name Required!!!!");
        return false;
    }
    if (form.kinnumber.value === ""){
        showError("kinnumber-error", "Next of Kin's Number Required!!!!");
        return false;
    }
    if (form.numberfarm.value === "select number of farms"){
        showError("numberfarm-error", "Number of Farm Required!!!!");
        return false;
    }
    if (form.farminyears.value === ""){
        showError("farminyears-error", "Number of years in farming Required!!!!");
        return false;
    }
    if (form.averageyield.value === ""){
        showError("averageyield-error", "Average yield Required!!!!");
        return false;
    }
    if (form.previousyield.value === ""){
        showError("previousyield-error", "Previous yield Required!!!!");
        return false;
    }
    if (form.farmbenefit.value === ""){
        showError("farmbenefit-error", "Benefit from farm Required!!!!");
        return false;
    }
    if (form.buyer.value === ""){
        showError("buyer-error", "Buyer of produce Required!!!!");
        return false;
    }
    if (form.selltime.value === ""){
        showError("selltime-error", " Required!!!!");
        return false;
    }

    if (form.buyerbenefits.value === ""){
        showError("buyerbenefits-error", " Required!!!!");
        return false;
    }

    if (form.funduses.value === ""){
        showError("funduses-error", "Required!!!!");
        return false;
    }
    document.querySelector(".success").classList.add("display-success");
    document.querySelector(".success").innerHTML="Your registeration was sucessfull";
    
    
}
// end form.validators//


// form-image-display-handler//
const image_upload = document.querySelector("#id_image1");
image_upload.addEventListener("change", function() {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_image = reader.result;
    document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
  });
  reader.readAsDataURL(this.files[0]);
});
// end form-image-display-handler//
