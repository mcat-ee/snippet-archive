//If on the 'Members' page for a group will automatically get the next set of paginated group members
function getMore() { 
	var elements = document.getElementsByClassName("pam uiBoxLightblue uiMorePagerPrimary");
	var element = elements[0];
	element.click();
}
