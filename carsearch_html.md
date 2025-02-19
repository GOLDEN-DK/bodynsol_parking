<body>
	<aside id="lnb" class="animated">
	<button type="button" class="btn-lnb-slide show"></button>
	<button type="button" class="btn-lnb-slide hide"></button>
	<div class="scrollable lnb-holder animated">
<ul id="lnb-panels">
			<li class="lnb-panel">
					<h2 class="lnb-panel-title">조회</h2>
					<ul class="lnb-panel-menus">
					<li class="lnb-panel-menu-holder ">
							<a class="lnb-panel-menu" href="/cooperators/home">차량 조회</a>
						</li>
					</ul>
				</li>
			<li class="lnb-panel">
					<h2 class="lnb-panel-title">운영</h2>
					<ul class="lnb-panel-menus">
					<li class="lnb-panel-menu-holder ">
							<a class="lnb-panel-menu" href="/cooperators/visitcouponbooks/group">내 할인권 현황</a>
						</li>
					<li class="lnb-panel-menu-holder ">
							<a class="lnb-panel-menu" href="/cooperators/visitcoupons">쿠폰 발급 내역</a>
						</li>
					</ul>
				</li>
			<li class="lnb-panel">
					<h2 class="lnb-panel-title">관리</h2>
					<ul class="lnb-panel-menus">
					<li class="lnb-panel-menu-holder ">
							<a class="lnb-panel-menu" href="/cooperators/mypages">마이페이지</a>
						</li>
					</ul>
				</li>
			</ul>
		</div>
</aside>
<script>
(function($) {
	$(document).on('click', '.btn-lnb-slide.show', function (ev) {
		ev.preventDefault();
        
		$('#lnb').removeClass('fadeOutRight').addClass('active fadeInRight');
		$('.lnb-holder').show();
	}).on('click', '.btn-lnb-slide.hide', function (ev) {
		ev.preventDefault();
		
		$('#lnb').addClass('fadeOutRight').removeClass('active fadeInRight');
		$('.lnb-holder').hide();
    });
	
	
})(jQuery);
</script>
<div id="wrap">
		<header id="gnb">
	<div id="gnb-content">
		<h1 id="gnb-title-holder">
			<a id="gnb-title" href="/cooperators">주차시스템</a>&nbsp;<b id="district-name">궁동주차장</b>
		</h1>
		<div class="mobile-gnb-holder">
			<button type="button" class="btn-mobile-menu">MENU</button>
			<div class="mobile-gnb-menu-holder">
				<div class="mobile-gnb-bg"></div>
				<div class="mobile-gnb-menu">
					<ul id="gnb-menus">
						<li class="gnb-menu-holder member">
									<a href="/cooperators/mypages" class="member-name">바디앤솔 필라테스</a><a href="#" id="btn-logout" class="link gnb-menu">로그아웃</a>
									<button class="mobile-gnb-close"></button>
								</li>
							</ul>
					<ul id="lnb-panels">
						<li class="lnb-panel-menu-holder category-emoticon search">
									<h2 class="lnb-panel-title">조회</h2>
									<ul class="lnb-panel-menus">
									<li class="lnb-panel-menu-holder ">
											<a class="lnb-panel-menu" id="menu-url" href="/cooperators/home">차량 조회</a>
										</li>
									</ul>
								</li>						
							<li class="lnb-panel-menu-holder category-emoticon operation">
									<h2 class="lnb-panel-title">운영</h2>
									<ul class="lnb-panel-menus">
									<li class="lnb-panel-menu-holder ">
											<a class="lnb-panel-menu" id="menu-url" href="/cooperators/visitcouponbooks/group">내 할인권 현황</a>
										</li>
									<li class="lnb-panel-menu-holder ">
											<a class="lnb-panel-menu" id="menu-url" href="/cooperators/visitcoupons">쿠폰 발급 내역</a>
										</li>
									</ul>
								</li>						
							<li class="lnb-panel-menu-holder category-emoticon management">
									<h2 class="lnb-panel-title">관리</h2>
									<ul class="lnb-panel-menus">
									<li class="lnb-panel-menu-holder ">
											<a class="lnb-panel-menu" id="menu-url" href="/cooperators/mypages">마이페이지</a>
										</li>
									</ul>
								</li>						
							</ul>
					<!-- 
					<div class="btn-holder">
						<button id="btn-logout" class="btn gnb-menu" type="button">로그아웃</button>
					</div>
					 -->
				</div>
			</div>
		</div>
	</div>
</header>
<script>
	var _districtMap = {};
	var _districts = [];
	var _district = __utils__.cookie('district');
	var _office = __utils__.cookie('office');
	var _districtCallback;

    $.cup.ajax({
    	url: '/api/v2/office',
    	success: function(res) {
    		_office = res.data.office;
    		//
    		$.cup.ajax({
    			url: '/api/v2/districts',
    			success: function (res) {
    				_districts = res.data.districts.list;

    				if ($.cup.member().details && $.cup.member().details.districtIds && $.cup.member().details.districtIds.length > 0) {
    					var myDistricts = $.cup.member().details.districtIds || [];
    					var shownDistricts = [];

    					$.cup.each(_districts, function (district, i) {
    						if (myDistricts.includes(district.id)) {
    							shownDistricts.push(district);
    							_districtMap[district.id] = district;
    						}
    					});
    					_districts = shownDistricts;
    				} else {
    					$.cup.each(_districts, function (district, i) {
    						_districtMap[district.id] = district;
    					});
    				}

    				if(_district) {
    					_district = JSON.parse(_district);
    				}else {
    					_district = _districts[0];
    				}
    				__utils__.cookie('district', JSON.stringify(_district));
    				setDistricts();

    				// if (_districtsCallback) {
    				// 	_districtsCallback();
    				// }

    				var emoticonList = ['search', 'operation', 'management'];
    				var emoticon = document.getElementsByClassName('category-emoticon');

    				for (var i = 0; i < emoticon.length; i++) {
    					emoticon[i].classList.add(emoticonList[i]);
    				}
    			}
    		});
    	}
    })


    function setDistricts() {
    	if (_districts.length > 1) {
    		_districts.unshift({code:'', name:_office.districtName + '(전체)'});

    		var $select = $('<select>').attr('id', 'gnb-district');
    		$('#district-name').html($select);
    		$.cup.each(_districts, function(district) {
    			var $option = $('<option>').val(district.id).text(district.name);
    			if(_district.id == district.id)
    				$option.prop('selected', true);
    			$select.append($option);
    		});

    		$select.on('change', function() {
    			_district = _districts[$(this).find('option:selected').index()];
    			__utils__.cookie('district', JSON.stringify(_district));
    			location.reload();
    		});
    	} else {
    		$('#district-name').text(_districts[0].name);
    		_district = _districts[0];
    	}

    	if(_district.details && _district.details.type == 'APT' && _district.details.reservations) {
    		$('.lnb-panel-menu-holder.search').hide();
    		$('.lnb-panel-menu-holder.operation .lnb-panel-menu-holder.visitcoupons').hide();
    	}
    	if(_district.details && !_district.details.preRegisteredVisitCoupons) {
    		$('.menu-reservation').hide();
    		$('#previsit-coupon-create').hide();
    	}
    	$('title').text(((_office.districtName)? _office.districtName + ' | ' : '') + $('title').text() );
    }

    function refreshDistrict(districtUpdated) {
    	$.cup.each(_districts, function(district, i) {
    		if(district.id == districtUpdated.id) {
    			_districts[i] = districtUpdated;
    			if(_district.id == districtUpdated.id) {
    				_district = districtUpdated;
    				__utils__.cookie('district', JSON.stringify(_district));
    			}
    			return false;
    		}
    	});
    }

(function($) {
/_
$('.btn-mobile-menu').on('click', function() {
$('.mobile-gnb-menu-holder').toggle('slide');
$(this).toggleClass('clear');
});
_/
$(document).on('click', '.btn-mobile-menu', function(ev) {
ev.preventDefault();
$('.mobile-gnb-menu-holder').fadeIn();
$('.mobile-gnb-menu').animate({right: 0}, {duration: 500});
}).on('click', '.mobile-gnb-close', function(ev) {
ev.preventDefault();
$('.mobile-gnb-menu-holder').fadeOut();
$('.mobile-gnb-menu').animate({right: '-320px'}, {duration: 500});
}).on('click', '.lnb-panel-title', function(ev) {
ev.preventDefault();
$(this).parent().find('.lnb-panel-menus').slideToggle(300);
});
})(jQuery);
</script>

<div id="container">
			<div id="main">
				<div>
					<div id="app">
						<div id="app-head">
							<div class=""></div>
							<h3 id="app-title" class="car-search-title" style="float:left;width:100%;">차량 조회
<span class="reset-time-holder">
									남은시간 <span class="reset-time"></span>초
								</span>
							</h3>
							<!-- 
							<div id="app-head-menus">
								<button id="visit-coupon-create" class="btn btn-primary" type="button">할인권 등록</button>
							</div>
							 -->
						</div>
						<div class="app-section-body box-style" id="notice-pop" style="float:right;margin-top:-55px; display:none; cursor:pointer;">
							<div class="notice-head" style="padding:0 0 0 25px; margin:-16px -12px 0 -13px;height:20px;">
								<span class="icon btn-pop"></span>
							</div>
						</div>
						<div id="app-body" style="clear:both;display:block;">
							<section class="app-section app-section-full-width app-section-tailless">
<div class="app-section-body box-style" style="clear:both;">
									<form id="page-filter" class="qbox clear-both" method="get">
										<ul class="qbox-filters">
											<li class="qbox-filter clear-both">
<div class="qbox-filter-field align_left qbox-filter-lpn"><input id="visit-lpn" name="lpn" value="" class="tbox" placeholder="차량번호 4자리" type="text" autocomplete="off"></div>
											</li>
										</ul>
										<div class="qbox-buttons">
											<input name="leaved" value="false" type="hidden">
											<input name="page" value="0" type="hidden">
											<input name="size" value="10" type="hidden">
											<input name="sort" value="entered_d" type="hidden">
											<button id="btn-init" class="btn" type="button">초기화</button>
											<button id="keyboard" class="btn btn-primary" type="button">가상키보드</button>
											<button id="btn-find" class="btn btn-primary" type="button">조회</button>
										</div>
									</form>
								</div>
							</section>
							<section class="app-section app-section-full-width app-section-tailless phase2-section" style="display:none;">
								<input type="hidden" id="useAutoBackHome" value="">
								<div class="app-section-body">
									<p style="font-size:12px;padding:0 0 5px 5px">일반형 할인권</p>
									<div id="visit-coupon-book-holder" class="page"><table class="gbox-table">
		<thead class="gbox-head">			
			<tr class="gbox-head-row">
					<th class="gbox-head-cell">쿠폰 종류</th>
					<th class="gbox-head-cell">유/무료</th>
					<th class="gbox-head-cell">할당 수량</th>
					<th class="gbox-head-cell">잔여 수량</th>
			</tr>
		</thead>
		<tbody class="gbox-body">
					<tr class="gbox-body-row" data-record="{&quot;amount&quot;:null,&quot;code&quot;:null,&quot;templateId&quot;:8,&quot;notFree&quot;:0,&quot;totalNumberOfIssuance&quot;:7683,&quot;name&quot;:&quot;1시간(유료)&quot;,&quot;id&quot;:11,&quot;feeFixing&quot;:null,&quot;oneDay&quot;:null,&quot;rate&quot;:null,&quot;issuedCount&quot;:7583,&quot;details&quot;:&quot;{}&quot;,&quot;minutes&quot;:60,&quot;couponIssueConstraint&quot;:null,&quot;estimatedAmount&quot;:null,&quot;fixable&quot;:0}">
							<td class="gbox-body-cell">1시간(유료)</td>
							<td class="gbox-body-cell"><b style="color: #2196f3;">무료</b></td>
							<td class="gbox-body-cell">7683</td>
							<td class="gbox-body-cell">100</td>
					</tr>
					<tr class="gbox-body-row" data-record="{&quot;issuedCount&quot;:300,&quot;totalNumberOfIssuance&quot;:300,&quot;amount&quot;:null,&quot;code&quot;:null,&quot;notFree&quot;:0,&quot;templateId&quot;:2,&quot;id&quot;:235,&quot;feeFixing&quot;:null,&quot;oneDay&quot;:null,&quot;rate&quot;:null,&quot;name&quot;:&quot;1시간할인권&quot;,&quot;details&quot;:&quot;{}&quot;,&quot;minutes&quot;:60,&quot;couponIssueConstraint&quot;:null,&quot;estimatedAmount&quot;:null,&quot;fixable&quot;:0}">
							<td class="gbox-body-cell">1시간할인권</td>
							<td class="gbox-body-cell"><b style="color: #2196f3;">무료</b></td>
							<td class="gbox-body-cell">300</td>
							<td class="gbox-body-cell">0</td>
					</tr>
					<tr class="gbox-body-row" data-record="{&quot;amount&quot;:null,&quot;code&quot;:null,&quot;notFree&quot;:0,&quot;templateId&quot;:9,&quot;issuedCount&quot;:7458,&quot;totalNumberOfIssuance&quot;:7557,&quot;feeFixing&quot;:null,&quot;oneDay&quot;:null,&quot;id&quot;:10,&quot;rate&quot;:null,&quot;minutes&quot;:30,&quot;details&quot;:&quot;{}&quot;,&quot;couponIssueConstraint&quot;:null,&quot;name&quot;:&quot;30분(유료)&quot;,&quot;estimatedAmount&quot;:null,&quot;fixable&quot;:0}">
							<td class="gbox-body-cell">30분(유료)</td>
							<td class="gbox-body-cell"><b style="color: #2196f3;">무료</b></td>
							<td class="gbox-body-cell">7557</td>
							<td class="gbox-body-cell">99</td>
					</tr>
		</tbody>
	</table></div>
								</div>
								<div class="app-section-body" style="display: none;">
									<p style="font-size:12px;padding:10px 0 5px 5px">포인트형 할인권</p>
									<div id="visit-coupon-balance-holder" class="page"></div>
								</div>
							</section>
							<section class="app-section app-section-full-width app-section-tailless">
<div class="app-section-body">
<!-- 									<div id="page-view" class="page"></div> -->
									<div id="page-view" class="gbox"></div>
								</div>
							</section>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- footer -->
<div class="footer-buttons">
	<div class="footer-buttons-background"></div>
	<div class="footer-buttons-content" style="margin-right: 8%;"></div>
	<div class="footer-buttons-content">
		<button id="btn-home" class="btn-footer" type="button">홈으로 이동</button>
	</div>
	<div class="footer-buttons-content">
		<button id="btn-up" class="btn-footer-up-img align_right" type="button"></button>
	</div>
</div>
<script type="text/javascript">

    $(document).on('click', '#btn-home', function() {
    	location.replace('/cooperators/home');
    }).on('click', '#btn-up', function() {
    	window.scrollTo(0, 0);
    });

</script></div>
<script id="toast-template" type="text/x-handlebars-template">
<div class="toast-holder{{text alerts ' toast-alert'}}">
<p class="toast-message">{{message}}</p>
</div>
</script>

<script id="toast-template-web-discount" type="text/x-handlebars-template">
	<div class="toast-holder{{text alerts ' toast-alert'}}">
		<p class="toast-message" style="font-size:20px;">{{message}}</p>
	</div>
</script>

<script id="lock-template" type="text/x-handlebars-template">
	<div id="{{id}}" class="lock-holder">
		<div class="lock-image-holder">
			<img src="/resources/img/jquery.cup/lock.gif" alt="Waiting">
			<p class="lock-caption">Waiting</p>
		</div>
	</div>
</script>
<script id="dialog-template" type="text/x-handlebars-template">
	<div class="dialog-holder{{attach prevDialog 'dialog-holder-transpaernt'}}{{attach classes}}">
		<div class="dialog">
			<div class="dialog-head">
				<h4 class="dialog-title">{{title}}</h4>
				<button class="dialog-close" type="button">Close</button>
			</div>
			<div class="dialog-body"></div>
			<div class="dialog-tail"></div>
		</div>
	</div>
</script>
<script id="dialog-tail-template" type="text/x-handlebars-template">
	{{#if (notEmpty tailButtons)}}
		{{#each tailButtons}}
			<button{{attr 'id' token}} class="btn{{attach (eq handler false) 'dialog-close'}}{{attach primary 'btn-primary'}}" type="button">{{label}}</button>
		{{/each}}
	{{/if}}
</script>
<script id="finder-template" type="text/x-handlebars-template">
	<div class="dialog-holder{{attach prevDialog 'dialog-holder-transpaernt'}}{{attach classes}}">
		<div class="dialog">
			<div class="dialog-head">
				<h4 class="dialog-title">{{title}}</h4>
				<button class="dialog-close" type="button">Close</button>
			</div>
			<div class="dialog-body"></div>
			<div class="dialog-tail">
				<button class="btn btn-primary dialog-close" type="button">닫기</button>
			</div>
		</div>
	</div>
</script>
<script id="gbox-table-template" type="text/x-handlebars-template">
	<table class="gbox-table">
		<thead class="gbox-head">			
			<tr class="gbox-head-row">
				{{#each columns}}
					<th class="gbox-head-cell"{{attach (attr 'style' styles)}}>{{text label}}</th>
				{{/each}}
			</tr>
		</thead>
		<tbody class="gbox-body">
			{{#if (notEmpty records)}}
				{{#each records}}
					<tr class="gbox-body-row" data-record="{{json this (not @root.__escapes__)}}">
						{{#each ../columns}}
							<td class="gbox-body-cell{{attach classes}}"{{attach (attr 'style' styles)}}>{{render ../this render}}</td>
						{{/each}}
					</tr>
				{{/each}}
			{{else}}
				<tr class="gbox-body-row ">
					<td class="gbox-body-cell gbox-body-cell-empty" colspan="{{length columns}}">
						데이터 없음
					</td>
				</tr>
			{{/if}}
		</tbody>
	</table>
</script>
<script id="page-template" type="text/x-handlebars-template">
	<div class="page-head">
		{{#if (eq paging.totalItems 0)}}
			<p class="page-count page-count-empty">총 0개</p>
		{{else}}
			<p class="page-count">총 {{paging.totalItems}}개 ({{add paging.page 1}}페이지 / {{paging.totalPages}}페이지)</p>
		{{/if}}
	</div>
	<div class="page-body">
		<div class="gbox"></div>
	</div>
	<div class="page-tail">
		{{#if (and (ne paging.first paging.page) (gte paging.first 0))}}
			<div class="page-nav page-nav-first">
				<a href="{{render paging.first url}}" class="page-nav-index">처음</a>
			</div>
		{{/if}}
		{{#if (and (ne paging.prev paging.page) (gte paging.prev 0))}}
			<div class="page-nav page-nav-prev">
				<a href="{{render paging.prev url}}" class="page-nav-index">이전</a>
			</div>
		{{/if}}
		{{#if (gt paging.siblings.length 0)}}
			<ul class="page-nav page-nav-siblings">
				{{#each paging.siblings}}
					<li class="page-nav-sibling">
						{{#if (eq this ../paging.page)}}
							<span class="page-nav-index">{{add this 1}}</span>
						{{else}}
							<a href="{{render this ../url}}" class="page-nav-index">{{add this 1}}</a>
						{{/if}}
					</li>
				{{/each}}
			</ul>
		{{/if}}
		{{#if (and (ne paging.next paging.page) (gte paging.next 0))}}
			<div class="page-nav page-nav-next">
				<a href="{{render paging.next url}}" class="page-nav-index">다음</a>
			</div>
		{{/if}}
		{{#if (and (ne paging.last paging.page) (gte paging.last 0))}}
			<div class="page-nav page-nav-last">
				<a href="{{render paging.last url}}" class="page-nav-index">마지막</a>
			</div>
		{{/if}}
	</div>
</script>
<script id="manual-leave-dialog-template" type="text/x-handlebars-template">
	<section class="app-section app-section-tailless">
		<div class="app-section-head">
			<h5 class="app-section-title">출차 정보</h5>	
		</div>
		<div class="app-section-body">
			<div class="field">
				<div class="field-head">
					<label for="visit-lpn" class="field-label">차량등록번호</label>
				</div>
				<div class="field-body">
					<input id="visit-lpn" name="lpn" class="tbox" maxlength="12" type="text" autocomplete="off" value="{{lpn}}">
				</div>
			</div>				
			<div class="field">
				<div class="field-head">
					<label for="manual-leave-remark" class="field-label">사유</label>
				</div>
				<div class="field-body">
					<textarea id="manual-leave-remark" name="manualLeaveRemark" class="ebox" maxlength="1024"></textarea>
				</div>
			</div>
		</div>
	</section>
</script>
<script>
	function manualLeave(visit, success) {
		var dialog = $.cup.dialog({
			title: '수동 출차',
			bodyTemplateId: 'manual-leave-dialog-template',
			data: {
				lpn: (visit)? visit.lpn : null
			},
			tailButtons: [{
				label: '취소',
				handler: false
			}, {
				label: '출차',
				primary: true,
				handler: function(ev) {
					if(!visit) {
						$.cup.submit(this, {
							method: 'post',
							url: '/api/v2/visits',
							validators: [{
								path: 'lpn'
							}, {
								path: 'manualLeaveRemark',
								determine: function(dVal, data) {
									return $.cup.isValid(dVal);
								},
								message: '사유를 입력해주세요.'
							}],
							parameterize: function(data) {
								visit = {
									districtId: 1,
									lpn: data.lpn,
									entered: $.cup.days().format('YYYY-MM-DDTHH:mm:ss'),
									details: {
										manualLeaveRemark: data.manualLeaveRemark
									}
								};
								return visit;
							},
							success: function(res) {
								visit.id = res.data.visitId;
								$.cup.ajax({
									url: '/api/v2/visits/' + visit.id,
									method: 'patch',
									params: {
				 						fields: ['details'],
										details: visit.details
									},
									success: function(res) {
										success();
										dialog.close();
									}
								});
							}
						});
					} else {
						$.cup.submit(this, {
							url: '/api/v2/visits/' + visit.id,
							method: 'patch', 
							parameterize: function(data) {
								visit.details.manualLeaveRemark = data.manualLeaveRemark; 
								return {
			 						fields: ['details'],
									details: visit.details
								};
							},
							validators: [{
								path: 'manualLeaveRemark',
								determine: function(dVal, data) {
									return $.cup.isValid(dVal);
								},
								message: '사유를 입력해주세요.'
							}],
							success: function(res) {
								success();
								dialog.close();
							}
						});
					}
				}
			}],
//			afterOpen: function() {
//			},
			trigger: this
		});
	}
</script>

<script id="api-detail-dialog-template" type="text/x-handlebars-template">
	<section class="app-section app-section-tailless">
		<div class="app-section-head">
			<h5 class="app-section-title">API 연동 상세</h5>
		</div>
		<div class="app-section-body">
			<div class="field">
				<div class="field-head">
					<label for="api-request" class="field-label">요청</label>
				</div>
				<div class="field-body">
					<textarea id="api-request" name="sb_request" class="ebox" maxlength="2048" style="width: 400px; height: 200px;">{{sb_request}}</textarea>
				</div>
			</div>
			<div class="field">
				<div class="field-head">
					<label for="api-response" class="field-label">결과</label>
				</div>
				<div class="field-body">
					<textarea id="api-response" name="sb_response_string" class="ebox" maxlength="2048">{{sb_response_string}}</textarea>
				</div>
			</div>
		</div>
	</section>
</script>
<script>
	(function($) {
		$(document).on('click', '.api-request', function(e) {
			if(!confirm('API를 전송하시겠습니까?'))
				e.preventDefault();
			location.reload();
		}).on('click', '.api-details', function() {
			var $record = $(this).closest('tr').data('record');
			var dialog = $.cup.dialog({
				title: 'API 연동 결과',
				bodyTemplateId: 'api-detail-dialog-template',
				data: $record.details,
				tailButtons: [{
					label: '닫기',
					handler: false
				}, {
					label: '재전송',
					primary: true,
					handler: function(ev) {
						$.cup.ajax({
							url: '/api/v2/visits/' + $record.id + '/sb/inout/',
							success: function(res) {
								console.log(res);
								dialog.close();
								location.reload();
							}
						});
					}
				}],
				trigger: this
			});
		}).on('click', '#sb-api-request', function() {
			var $check = $('input[type=checkbox]:checked').not('#cbox-all');
			if(!confirm($.cup.format('총 {0} 건을  요청하시겠습니까?', $check.length))) {
				return;
			}
			$.cup.each($check, function(v) {
				var $record = $(v).closest('tr').data('record');
				if($record) {
					$.cup.ajax({
						url: '/api/v2/visits/'+$record.id+'/sb/inout',
						method: 'get', 
						success: function(res) {
							console.log(res);
						}
					});
					sleep(100);	// 중요
				}
			});
			location.reload();
		});
		function sleep(delay) {
		    var start = new Date().getTime();
		    while (new Date().getTime() < start + delay);
		}
		
		$(document).on('click', '#cbox-all', function() {
			var checked = $(this).is(':checked');
			$('input[type=checkbox]').attr('checked', checked);
		});
	})(jQuery);
</script><script id="visit-memo-dialog-template" type="text/x-handlebars-template">

    	<div class="app-section-body">
    		<div class="field clear-both">
    			<div class="field-head align_left">
    				<label for="visit-memo" class="field-label">내용</label>
    			</div>
    			<div class="field-body align_left">
    				<textarea id="visit-memo" name="mem" class="ebox" maxlength="2048" style="height:200px">{{memo}}</textarea>
    			</div>
    		</div>
    	</div>
    </script>
    <script id="keyboard-dialog-template" type="text/x-handlebars-template">
    	<section class="app-section-tailless">
    		<div class="app-section-body">
    				<div id="numericInput" >

<table id="keypad">
					        <tr>
					            <td class="key">1</td>
					            <td class="key">2</td>
					            <td class="key">3</td>
					        </tr>
					        <tr>
					            <td class="key">4</td>
					            <td class="key">5</td>
					            <td class="key">6</td>
					        </tr>
					        <tr>
					            <td class="key">7</td>
					            <td class="key">8</td>
					            <td class="key">9</td>
					        </tr>
					        <tr>
					            <td id="clr-btn" class="keyboard-btn">←</td>
					            <td class="key">0</td>
					            <td id="find-btn" class="keyboard-btn">조회</td>	
					        </tr>
					   </table>
				   </div>
				</div>				
		</section>		
    </script>
	<script>
		(function($) {
			var pageQuery = $.cup.pageQuery();
			var $pageView = $('#page-view');
			var interval;
			var availableBooks = [];

    		if('' != '') {

// loadAndRender();
\_districtCallback = loadAndRender;
}

    		loadResetTime();
    		renderNotice();
    		var _visit;

    		//디바이스 타입 가져오기
    		var getDeviceType = function() {
    		  var ua = navigator.userAgent;
    		  if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
    		    return "tablet";
    		  }
    		  if (
    		    /Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(
    		      ua
    		    )
    		  ) {
    		    return "mobile";
    		  }
    		  return "desktop";
    		};

    		if(getDeviceType() == "desktop"){
    			$('.qbox-filter-field').empty();
    			$('.qbox-filter-field').append('<input id="visit-lpn" name="lpn" value="" class="tbox" placeholder="차량번호 4자리" type="text" autocomplete="off">');

    		}

    		$("#visit-lpn").bind('keydown', function(ev) {
    			if (ev.keyCode === 13) {
    				ev.preventDefault();
    				visitLpnSearch();
    				$("#visit-lpn").blur();
    			}
    		});

    		$(document).on('click', '#btn-find', function(ev) {
    			visitLpnSearch();
    		});

    		function visitLpnSearch() {
    			if ($('#visit-lpn').val().length > 3) {
    				loadAndRender();
    			}else {
    				if($('#visit-lpn').val().length == 0) {
    					$pageView.empty();
    				}
    				$.cup.toast('차량번호 4자리 이상 입력해주세요');
    			}
    		}
    		$(document).on('click', '#keyboard', function(ev) {
    			virtualCalculator();
    		});
    		function virtualCalculator() {
    			var numBox = document.getElementById('visit-lpn');
    			numBox.value = '';
    			var dialog = $.cup.dialog({
    				title: '',
    				bodyTemplateId: 'keyboard-dialog-template',
    				afterOpen: function() {
    					$('#numericInput').parents('.dialog-body').addClass('background-color');
    					$('#numericInput').parents('.dialog-body').parents('.dialog').addClass('margin-top');
    					$('#numericInput').parents('.dialog-body').next().hide();
    					$('.dialog-head').hide();
    					$('#numericInput').parents('.dialog-holder').css("background", "none");
    					$('.key').mousedown(function(){
    						if (numBox.value.length <0){
    							numBox.value = numBox.value + this.innerHTML;
    						} else if(numBox.value.length > 3){
    							numBox.value = numBox.value.substring(0,4);
    						} else {
    							numBox.value = numBox.value + this.innerHTML;
    						}
    						event.stopPropagation();
    					});
    					$('.key').mouseup(function(){
    						if(numBox.value.length > 3){
    							dialog.close();
    							loadAndRender();
    						}
    					});


    					$('#clr-btn').click(function(){
    						if(this.innerHTML == '←'){
    							if(numBox.value.length > 0){
    								numBox.value = numBox.value.substring(0, numBox.value.length - 1);
    							}
    						}
    						event.stopPropagation();
    					});

    					$('#find-btn').click(function(){
    						if(this.innerHTML == '조회'){
    							if(numBox.value.length > 3){
    								$('#visit-lpn').val(numBox.value);
    								dialog.close();
    								loadAndRender();
    							}else {
    								if(numBox.value.length == 0) {
    									$pageView.empty();
    								}
    								$.cup.toast('차량번호 4자리 이상 입력해주세요');
    							}
    						}
    						event.stopPropagation();
    					});
    					$(document).on('click', function(e){
    						var container = $(".dialog-body");
    						if (!container.is(event.target) && !container.has(event.target).length) {
    							dialog.close();
    						}
    					});
    					$("#visit-lpn").on("keyup", function(ev) {
    						if ($(this).val().length > 3) {
    							ev.preventDefault();
    							loadAndRender();
    							$("#visit-lpn").blur();
    							dialog.close();
    						}
    					});
    				}
    			});
    		}

    		function loadResetTime() {
    			var timeCheck = localStorage.getItem('timeCheck') ? JSON.parse(localStorage.getItem('timeCheck')) : 0;
    			// $('#reset-time-option').val(timeCheck).prop("selected",true);
    			$('#reset-time-option').val(timeCheck);
    		}

    		// $(document).on('change', '#reset-time-option',function(){
    		// 	localStorage.setItem('timeCheck', this.value);
    		// });

    		function loadAndRender() {

// $.cup.lock(function(unlock) {
var params = pageQuery.scan();
if(\_district && \_district.id)
params.districtId = \_district.id;
$.cup.ajax({
url: '/api/v2/visits',
params: params,
success: function(res) {
var visitList = res.data.visits.list;
if(visitList) {
visitList.forEach(function(item){
item.now = res.info.published;
})
}

    						res.data.visits.list = visitList.filter(function(item){
    							if (item.seasonal === null) return true;

    							if (item.seasonTicket && item.seasonTicket.seasonTicketTemplate) {
    								return item.seasonTicket.seasonTicketTemplate.timetable.length > 0;
    							}
    						});

    						if(res.data.visits.list.length > 1) {
    							$pageView.table({
    								columns: [{
    									label: '차량번호',
    									styles: 'padding:5px',
    									render: function(visit) {
    										if (visit.subLpn == null || visit.subLpn == visit.lpn) {
    											return visit.lpn;
    										}

    										return visit.lpn + " | " + visit.subLpn;
    									}
    								}, {
    									label: '구역',
    									styles: 'padding:5px',
    									render: function(visit) {
    										return visit.district.name;
    									}
    								}, {
    									label: '구분',
    									styles: 'padding:5px',
    									render: function(visit) {
    										if((visit.seasonTicket && !visit.seasonTicket.dropped) || visit.seasonal)
    											return $.cup.format('<b style="color: {0};">{1}</b>', '#ff5c01', '정기');
    										else
    											return '일반';
    									}
    								},{
    									label: '입차시각',
    									styles: 'padding:5px',
    									render: function(visit) {
    										var $entered = $.cup.days(visit.entered);
    										if($entered.format('YYYY-MM-DD')==$.cup.days().format('YYYY-MM-DD'))
    											return $entered.format('HH:mm:ss');
    										else
    											return $entered.format('YYYY-MM-DD<br>HH:mm:ss');
    									}
    								}, {
    									label: '주차시간',
    									render: function(visit) {
    										return cnsl.durationString($.cup.days(visit.entered), (visit.settled)? $.cup.days(visit.settled) : (visit.leaved)? $.cup.days(visit.leaved) : $.cup.days(visit.now)) + ((visit.leaved)? '' : '+');
    									}
    								}],
    								records: res.data.visits.list,
    							});
    						} else if(res.data.visits.list.length == 1) {
    							_visit = res.data.visits.list[0];
    							renderVisit(true,true);
    						} else {
    							$.cup.toast('입차 정보를 찾을 수 없습니다.');
    						}
    					}

// end: unlock
});
// });
}

    		function renderVisit(success, findFlag = false) {
    			if(!_visit)
    				return;
    			if(_visit.settled && !findFlag) {
    				renderVisitDetail(success);
    				return;
    			}

// if(\_visit.payed) {
// $.cup.toast('이미 결제되었습니다.');
// return;
// }
\_visit.settled = $.cup.days().format('YYYY-MM-DDTHH:mm:ss');
$.cup.lock(function(unlock) {
$.cup.ajax({
url: '/api/v2/charges/cooperators',
method: 'post',
params: {
visitId: \_visit.id,
synced: true,
//settled: \_visit.settled
},
success: function(res) {
if(!res.data.bill) {
$.cup.toast('요금 계산 오류입니다.');
return;
}
\_visit = res.data.visit;
\_visit.bill = res.data.bill;

    						renderVisitDetail(success);
    					},
    					end: unlock
    				});
    			});
    		}

    		function renderVisitDetail(success) {
    			$.cup.ajax({
    				url: '/api/v2/members/' + $.cup.member().id + '/availablebooks',
    				params: {
    					districtId: _visit.district.id,
    				},
    				success: function(res) {
    					var visitCouponBooks = res.data.availableBooks;
    					$.cup.each(res.data.availableBooks, function(book) {
    						book.details = JSON.parse(book.details);
    					});

    					var published = $.cup.days(res.info.published);
    					_visit.settled = res.info.published;
    							// 발급된 쿠폰 검색
    							$.cup.ajax({
    								url: '/api/v2/visitcoupons',
    								params: {
    									visitId: _visit.id,
    									size: 100
    								},
    								success: function(res) {
    									var visitCoupons = res.data.visitCoupons.list;
    									$.cup.each(visitCoupons, function(visitCoupon) {
    										$.cup.each(visitCouponBooks, function(visitCouponBook) {
    											if(visitCoupon.code == visitCouponBook.id) {
    												visitCoupon.name = visitCouponBook.name;
    												return false;
    											}
    										});
    									});

    									//--- 현장별 특별조치
    									if(_visit.district.code == 'crzm') {
    										if($.cup.member().details && $.cup.member().details['1x4']) {
    											visitCouponBooks.push({
    												visitCouponTemplate: {
    													code: '1x4',
    													name: '4시간'
    												}
    											})
    										}
    										if($.cup.member().details && $.cup.member().details['1x2']) {
    											visitCouponBooks.push({
    												visitCouponTemplate: {
    													code: '1x2',
    													name: '2시간'
    												}
    											})
    										}
    									}

    									// -- 버튼 disable 조건 처리
    									// -- published 는 서버에서 답신 줄때 주는 서버 시간이므로 해당 시간으로 활용한다.
    									isButtonDisableForVisitCouponBooks(visitCouponBooks, published);

    									//---

    									loadAndBuildBalance(function(balances) {
    										$.cup.each(balances, function (balance) {
    											if (balance.specialUsage === 'TIME_DEDUCTION') {
    												var balanceId = balance.templateId;

    												$.cup.each(visitCoupons, function (visitCoupon) {
    													if (visitCoupon.visitCouponTemplate.id === balanceId) {
    														balance.disabled = true;
    													}
    												});
    											}
    										});

    										$pageView.empty().append($.cup.template('coupon-control-template').build({
    											visit: _visit,
    											duration: cnsl.durationString($.cup.days(_visit.entered), $.cup.days(_visit.settled)),
    											visitCoupons: visitCoupons,
    											visitCouponBooks: visitCouponBooks,
    											visitCouponBalances: balances,
    											member: $.cup.member()
    										}).toString());

    										$pageView.find('.gbox-body-cell img').on('error', function() {
    											$(this).attr('src', '/resources/img/bg-main.jpg');
    										});

    										if(success) {
    											success();
    										}

    										if(interval) {
    											clearInterval(interval);
    										}

    										// $('#reset-time-option').hide();
    										var reset = localStorage.getItem('timeCheck') ? JSON.parse(localStorage.getItem('timeCheck')) : 0;

    										if (reset > 0) {
    											interval = setInterval(function() {
    												$('.reset-time-holder').show().find('.reset-time').text(reset--);
    												$('.reset-time-holder').css("display", "inline-block");

    												if(reset == 0) {
    													location.href = '/cooperators';
    													$('.reset-time-holder').hide();
    													// $('#reset-time-option').show();
    												}
    											}, 1000)
    										}
    									});
    								}
    							});
    						// }
    					// });

    					//FIXME: sts1, akc1 : CouponBook 세팅 필요
    					/*//---
    					$.cup.ajax({
    						url: '/api/v2/visitcoupontemplates',
    						params: {
    							size: 100
    						},
    						success: function(res) {
    							var visitCouponPlans;
    							if($('#district-name').data('district').code == 'sts1') {
    								visitCouponPlans = [{
    									code: 1, minutes: 60, name: '1시간 할인'
    								},{
    									code: 3, minutes: 180, name: '3시간 할인'
    								},{
    									code: 6, minutes: 360, name: '6시간 할인'
    								},{
    									code: 24, minutes: 1440, name: '24시간 할인'
    								}];
    							} else {
    								visitCouponPlans = res.data.visitCouponTemplates.list;
    								$.cup.each(visitCouponPlans, function(visitCouponPlan) {
    									$.cup.each(visitCouponBooks, function(visitCouponBook) {
    										if(visitCouponBook.visitCouponTemplate.id == visitCouponPlan.id) {
    											visitCouponPlan.visitCouponBook = visitCouponBook;
    											return false;
    										}
    									});
    								});
    							}

    							//FIXME---
    							$.cup.each(visitCouponPlans, function(visitCouponPlan) {
    								if($('#district-name').data('district').code == 'akc1') {
    									if($.cup.member().id == 14
    										&& visitCouponPlan.code == '1') {
    										visitCouponPlan.disabled = true;
    									} else if(($.cup.member().id == 23
    												|| $.cup.member().id == 24)
    											&& (visitCouponPlan.code == '1'
    												|| visitCouponPlan.code == '2')) {
    										visitCouponPlan.disabled = true;
    									} else if(($.cup.member().id == 25)
    											&& (visitCouponPlan.code == '2')) {
    										visitCouponPlan.disabled = true;
    									}
    								}
    							});
    							//---

    							$.cup.ajax({
    								url: '/api/v2/visitcoupons',
    								params: {
    									visitId: _visit.id,
    									size: 100
    								},
    								success: function(res) {
    									var visitCoupons = res.data.visitCoupons.list;

    									var type = '';
    									if(_visit.bill.finalFee == null) {
    										$.cup.toast('출구에서 정산해주세요.');
    										return;
    									} else if(_visit.seasonTicket) {
    										$.cup.toast('정기권 차량입니다.');
    										return;
    									}

    									$.cup.each(visitCoupons, function(visitCoupon) {
    										$.cup.each(visitCouponPlans, function(visitCouponPlan) {
    											if(visitCoupon.code == visitCouponPlan.code) {
    												visitCoupon.name = visitCouponPlan.name;
    												return false;
    											}
    										});
    									});

    									$('#page-view').empty().append($.cup.template('coupon-control-template').build({
    										visit: _visit,
    										duration: cnsl.durationString($.cup.days(_visit.entered), $.cup.days(_visit.settled)),
    										visitCoupons: visitCoupons,
    										visitCouponPlans: visitCouponPlans,
    										member: $.cup.member()
    									}).toString());

    									$pageView.find('.gbox-body-cell img').on('error', function() {
    										$(this).attr('src', '/resources/img/bg-main.jpg');
    									});

    									if(success)
    										success();
    								}
    							});
    						}
    					});
    					*///---
    				}
    			});
    		}

    		/**
    		 * 운영자 쿠폰북에 대해 버튼이 비활성화되어야 하는지 확인합니다.
    		 * @param {Array} visitCouponBooks - 운영자 쿠폰북의 배열
    		 * @param {string} published - 서버 시간
    		 */
    		function isButtonDisableForVisitCouponBooks(visitCouponBooks, published) {
    			$.cup.each(visitCouponBooks, function(visitCouponBook) {
    				visitCouponBook.isButtonDisable = false;

    				if (!$.cup.isEmpty(visitCouponBook.couponIssueConstraint)) {
    					visitCouponBook.couponIssueConstraint = JSON.parse(visitCouponBook.couponIssueConstraint)
    				}

    				// 발급 가능 수량 여부 확인
    				if(!$.cup.isEmpty(visitCouponBook.totalNumberOfIssuance)) {
    					if (Number(visitCouponBook.totalNumberOfIssuance) - Number(visitCouponBook.issuedCount) <= 0) {
    						visitCouponBook.isButtonDisable = true;
    						return true;
    					}
    				}

    				// 발급 가능 여부 확인
    				if (visitCouponBook.couponIssueConstraint) {
    					var issueTimeApproval = visitCouponBook.couponIssueConstraint.issueTimeApproval

    					if (!$.cup.isEmpty(issueTimeApproval)) {
    						var timeStandard = issueTimeApproval.timeStandard;
    						var start = issueTimeApproval.start.split(':');
    						var end = issueTimeApproval.end.split(':');

    						var baseDateTime = timeStandard === 'ENTERED' ? $.cup.days(_visit.entered) : published;
    						var dateStartObj = baseDateTime.hour(start[0]).minute(start[1]).second(start[2]);
    						var dateEndObj = baseDateTime.hour(end[0]).minute(end[1]).second(end[2]);

    						if (isNotInPermittedTimeRange(baseDateTime, dateStartObj, dateEndObj)) {
    							visitCouponBook.isButtonDisable = true;
    							return true;
    						}
    					}
    				}
    			});
    		}

    		function isNotInPermittedTimeRange(baseDateTime, issueDateTimeStart, issueDateTimeEnd) {
    			return !isInPermittedTimeRange(baseDateTime, issueDateTimeStart, issueDateTimeEnd)
    		}

    		function isInPermittedTimeRange(baseDateTime, issueDateTimeStart, issueDateTimeEnd) {
    			var durations = [];

    			if (issueDateTimeEnd.isBefore(issueDateTimeStart)) {
    				durations.push({
    					'start': issueDateTimeStart.subtract(1, 'day'),
    					'end': issueDateTimeEnd
    				});

    				durations.push({
    					'start': issueDateTimeStart,
    					'end': issueDateTimeEnd.add(1, 'day')
    				});

    				var isInPermittedTimeRange = false;
    				durations.forEach(function (d, index) {
    					if (baseDateTime.isAfter(d.start) && baseDateTime.isBefore(d.end)) {
    						isInPermittedTimeRange = true;
    					}
    				});

    				return isInPermittedTimeRange;
    			} else {
    				return baseDateTime.isAfter(issueDateTimeStart) && baseDateTime.isBefore(issueDateTimeEnd);
    			}
    		}

    		function loadAndBuildBalance(callback) {
    			$.cup.ajax({
    				url: '/api/v2/visitcouponbalances',
    				params: $.cup.pageless({
    					sort: 'template.name',
    					memberId: '27',
    					unclosed: true
    				}),
    				success: function(res) {
    					var balances = [];

    					$("#useAutoBackHome").val();

    					$.cup.each(filterBalances(res.data.visitCouponBalances.list), function(balance) {
    						var buttons = [];
    						var template = balance.template;
    						var buttonEnabled = false;

    						if (balance.template.specialUsage === 'TIME_DEDUCTION') {
    							buttonEnabled = true;
    							var pointsBalance = balance.pointsBalance;
    							var dayStr = makeDateForm(pointsBalance);

    							balance.pointsBalance = pointsBalance + '(' + dayStr + ')';
    						}

    						$.cup.each(balance.template.buttons || [], function(button) {
    							var points, optionEnabled;
    							if(template.specialUsage == 'MIXED_CHARGE') {
    								points = Math.floor(button.point);
    							}else {
    								points = Math.floor(button.value * template.pointsPerUnit / template.unit);
    							}
    							optionEnabled = points <= balance.pointsBalance;
    							buttonEnabled = buttonEnabled || optionEnabled;

    							buttons.push({
    								label: button.label,
    								value: button.value,
    								point: button.point,
    								type: button.type,
    								disabled: !optionEnabled
    							});
    						});

    						balances.push({
    							id: balance.id,
    							name: template.name,
    							templateId: template.id,
    							buttons: buttons,
    							pointsBalance: balance.pointsBalance,
    							specialUsage: template.specialUsage,
    							disabled: !buttonEnabled
    						});
    					});

    					callback(balances);
    				}
    			});
    		}

    		var makeDateForm = function (min) {
    			var days = Math.floor(min / 60 / 24);
    			var hours = Math.floor((min - (days * 60 * 24 )) / 60);
    			var mins = min - (days * 60 * 24) - (hours * 60);

    			var daysStr = days;
    			var hourStr = (hours > 9)? hours : '0' + hours;
    			var minStr = (mins > 9)? mins : '0' + mins;

    			return daysStr + '일 ' + hourStr + '시간 ' + minStr + '분';
    		}

    		function renderNotice(){
    			var _params = pageQuery.scan();
    			_params.size = 10;
    			_params.sort = 'priority_a_start_d';
    			_params.isPublic = true;
    			$.cup.ajax({
    				method: 'get',
    				url: '/api/v2/notices',
    				params: _params,
    				success:function(res){
    					var notices = res.data.notices.list;
    					if(notices.length > 0) {
    						$('#notice-pop').show();
    						$(document).on('click', '#notice-pop', function(ev) {
    							var dialog = $.cup.dialog({
    								title: '<div class="notice-head"><span class="icon"></span>공지사항</div>',
    								bodyTemplateId: 'notice-body-template',
    								data: {
    									notices: notices,
    								},
    							});

    							// $('#app').prepend($.cup.template('notice-body-template').build({
    							// 	notices: notices
    							// }).toString());

    							var html = $.cup.template('notice-body-template').build(notices).toString();
    							$('#notice-pop').append(html);

    							var bodies = document.getElementsByClassName('notice-body');
    							$.each(bodies, function(i, contents){
    								$(this).empty().append('<pre class="notice-contents">'+notices[i].contents.trim()+'</pre>')
    							});
    						});
    					}
    				}
    			});
    		};

    		function goBackHomeAfterApplyCouponByOption() {
    			if ($("#useAutoBackHome").val()) {
    				$.cup.webdiscounttoast('할인처리되었습니다. 홈으로 이동합니다.', 4000);
    				setTimeout(() => {
    					location.replace('/cooperators/home');
    				}, 4000);
    			}
    		}

    		$(document).on('click', '#page-view .gbox-body-row', function() {
    			var record = $(this).closest('tr').data('record');
    			// 주의
    			if(record) {
    				_visit = record;
    				renderVisit();
    			}
    		}).on('click', '#btn-init', function() {

// location.replace('/cooperators');
location.href = '/cooperators';
}).on('click', '.btn-visit-coupon', function() {
var record = $(this).data('record');
var $btns = $('.btn-visit-coupon-prevent').prop('disabled', true);

    			// renderVisit을 먼저 호출하여 최신 정산 데이터 확인
    			renderVisit(function() {
    				/*//--- coupon 제한
    				if(_visit.district.code == 'akc1'
    					&& _visit.bill && _visit.bill.calcOption && _visit.bill.calcOption.visitCoupons.length > 0) {
    					var remained = 120 - record.minutes;
    					$.cup.each(_visit.bill.calcOption.visitCoupons, function(visitCoupon) {
    						if(visitCoupon.code == '1' || visitCoupon.code == '2') {
    							remained -= visitCoupon.minutes;
    						}
    					});
    					if(remained < 0
    						&& (record.code == '1' || record.code =='2')) {
    						$.cup.toast('더 이상 할인할 수 없습니다.');
    						return;
    					}
    				}
    				*///---
    				/*if(_visit.district.code == 'akc1') {
    					// 무료 쿠폰은 1장만 사용
    					if(record.code == '1' || record.code == '2' || record.code == '3') {
    						var count = 0;
    						$.cup.each(_visit.bill.calcOption.visitCoupons, function(visitCoupon) {
    							if(visitCoupon.code == '1' || visitCoupon.code == '2' || visitCoupon.code == '3') {
    								count++;
    								return false;
    							}
    						});
    						if(count > 0) {
    							$.cup.toast('무료 쿠폰은 1번 만 사용 가능합니다.', true);
    							return false;
    						}
    					}
    				} else if(_visit.district.code == 'crzm') {
    					if(record.code == '1') {
    						var count = 0;
    						$.cup.each(_visit.bill.calcOption.visitCoupons, function(visitCoupon) {
    							if(visitCoupon.code == '1') {
    								count++;
    							}
    						});
    						if(count > 1) {
    							$.cup.toast('무료 쿠폰은 2번 만 사용 가능합니다.', true);
    							return false;
    						}
    					} else if(record.code == '11' || record.code == '12') {
    						var count = 0;
    						$.cup.each(_visit.bill.calcOption.visitCoupons, function(visitCoupon) {
    							if(visitCoupon.code == '11' || visitCoupon.code == '12') {
    								count++;
    							}
    						});
    						if(count > 6) {
    							$.cup.toast('유료 쿠폰은 7번 만 사용 가능합니다.', true);
    							return false;
    						}
    					}
    				}*/

    				//--- 현장별 특별조치
    				if(_visit.district.code == 'crzm'
    					&& (record.code == '1x4'
    						|| record.code == '1x2')) {
    					var params = {
    							visitId: _visit.id,
    							code: 1,
    							minutes: 60,
    							visitCouponTemplateId: 1
    						}
    					if(record.code == '1x4') {
    						$.cup.ajax({
    							url: '/api/v2/visitcoupons',
    							method: 'post',
    							params: params,
    							success: function(res) {
    								renderVisit();
    								$.cup.ajax({
    									url: '/api/v2/visitcoupons',
    									method: 'post',
    									params: params,
    									success: function(res) {
    										renderVisit();
    										$.cup.ajax({
    											url: '/api/v2/visitcoupons',
    											method: 'post',
    											params: params,
    											success: function(res) {
    												renderVisit();
    												$.cup.ajax({
    													url: '/api/v2/visitcoupons',
    													method: 'post',
    													params: params,
    													success: function(res) {
    														_visit.settled = null;
    														renderVisit();
    														$.cup.ajax({
    									                        url: '/api/v2/machines',
    									                        params: {
    									                           type: 'PAY_STATION'
    									                        },
    									                        success: function(res) {
    									                           $.cup.each(res.data.machines.list, function(machine) {
    									                              $.cup.ajax({
    									                                 url: '/api/v2/machines/' + machine.code + '/state',
    									                                 success: function(res) {
    									                                    var visit = res.data.machine.visit;
    									                                    if(visit && visit.id == _visit.id) {
    									                                       // 요금 전송
    									                                       $.cup.ajax({
    									                                          url: '/api/v2/charges',
    									                                          method: 'post',
    									                                          params: {
    									                                             visitId: _visit.id,
    									                                             // 여기서는 settled가 정해져 있는 경우 변경하면 안됨
    									                                             settled: (_visit.settled)? _visit.settled : $.cup.days().format('YYYY-MM-DDTHH:mm:ss'),
    																				 synced: (!_visit.settled)? true : false,
    									                                             end: (_visit.settled)? _visit.settled : null,
    									                                             machineSettleCode: machine.code
    									                                          },
    									                                          success: function(res) {
    								                                        	  	if(res.data.visit.leaved) {
    								                                        	  		$.cup.toast('출차처리되었습니다.');
    																					location.replace('/cooperators/home');
    									                                        	}
    									                                          }
    									                                       });
    									                                    }
    									                                 }
    									                              });
    									                           });
    									                        }
    									                     });
    													},
    													end: function() {
    														$btns.prop('disabled', false);
    													}
    												});
    											}
    										});
    									}
    								});
    							},
    						});
    					} else if(record.code == '1x2') {
    						$.cup.ajax({
    							url: '/api/v2/visitcoupons',
    							method: 'post',
    							params: params,
    							success: function(res) {
    								renderVisit();
    								$.cup.ajax({
    									url: '/api/v2/visitcoupons',
    									method: 'post',
    									params: params,
    									success: function(res) {
    										_visit.settled = null;
    										renderVisit();
    										$.cup.ajax({
    					                        url: '/api/v2/machines',
    					                        params: {
    					                           type: 'PAY_STATION'
    					                        },
    					                        success: function(res) {
    					                           $.cup.each(res.data.machines.list, function(machine) {
    					                              $.cup.ajax({
    					                                 url: '/api/v2/machines/' + machine.code + '/state',
    					                                 success: function(res) {
    					                                    var visit = res.data.machine.visit;
    					                                    if(visit && visit.id == _visit.id) {
    					                                       // 요금 전송
    					                                       $.cup.ajax({
    					                                          url: '/api/v2/charges',
    					                                          method: 'post',
    					                                          params: {
    					                                             visitId: _visit.id,
    					                                             // 여기서는 settled가 정해져 있는 경우 변경하면 안됨
    					                                             settled: (_visit.settled)? _visit.settled : $.cup.days().format('YYYY-MM-DDTHH:mm:ss'),
    																 synced: (!_visit.settled)? true : false,
    					                                             end: (_visit.settled)? _visit.settled : null,
    					                                             machineSettleCode: machine.code
    					                                          },
    					                                          success: function(res) {
    				                                        	  	if(res.data.visit.leaved) {
    				                                        	  		$.cup.toast('출차처리되었습니다.');
    																	location.replace('/cooperators/home');
    					                                        	}
    					                                          }
    					                                       });
    					                                    }
    					                                 }
    					                              });
    					                           });
    					                        }
    					                     });
    									},
    									end: function() {
    										$btns.prop('disabled', false);
    									}
    								});
    							},
    						});
    					}
    					return;
    				//FIXME
    				}
    				else if(_visit.district.code == 'aysc' && (record.code == '1')) {
    					$.cup.ajax({
    						url: '/api/v2/charges',
    						method: 'post',
    						params: {
    							visitId: _visit.id,
    							machineSettleCode: $.cup.member().details.machineCode,
    							settled: _visit.settled,
    							fixedFee: record.amount
    						},
    						success: function(res) {
    							_visit = res.data.visit;
    							renderVisitDetail();
    						}
    					});
    					return;
    				}
    				//---
    				$.cup.ajax({
    					url: '/api/v2/visitcoupons',
    					method: 'post',
    					params: {
    						visitId: _visit.id,
    						code: record.code,
    						minutes: record.minutes,
    						amount: record.amount,
    						rate: record.rate,
    						feeFixing: record.feeFixing,
    						fixable: record.fixable == 'N' ? false : true, 	//fixable인 경우 amount=0 가능
    						reservedDistrictId: _visit.district.id,
    						visitCouponTemplateId: record.templateId,
    						oneDay: record.oneDay
    					},
    					success: function(res) {
    						_visit.settled = null;	// 재정산을 위해
    						renderVisit();
    						loadAndRenderBook();

    						var visitDistrict = _districtMap[_visit.district.id];

    						if(visitDistrict.details && visitDistrict.details.kioskChargeWhenCooperatorCoupon == false) {
    							goBackHomeAfterApplyCouponByOption();
    							return;
    						}

    						//--- 무인정산기에 해당 visit이 정산 중인지 확인
    						$.cup.ajax({
    							url: '/api/v2/machines',
    							params: {
    							   type: 'PAY_STATION'
    							},
    							success: function(res) {
    								if (record.details && record.details.payedWhenFree) {
    									chargeFee(_visit, null,record.details.payedWhenFree, function(res) {
    										// payedFee = 0 이면 자동으로 pay 처리 됨
    										$.cup.toast('결제처리되었습니다. 홈으로 이동합니다.');
    										setTimeout(() => {
    											location.replace('/cooperators/home');
    										}, 2000);
    									});
    								} else {
    									$.cup.each(res.data.machines.list, function(machine) {
    										$.cup.ajax({
    											url: '/api/v2/machines/' + machine.code + '/state',
    											success: function(res) {
    												var visit = res.data.machine.visit;
    												if(visit && visit.id == _visit.id) {
    													// 요금 전송
    													chargeFee(_visit, machine.code, false, function(res) {
    														if(res.data.visit.leaved) {
    															$.cup.toast('출차처리되었습니다. 홈으로 이동합니다.');
    															setTimeout(() => {
    																location.replace('/cooperators/home');
    															}, 2000);
    														}
    													});
    												}
    											}
    										});
    									});
    								}
    							}
    						});

    						goBackHomeAfterApplyCouponByOption();
    					}
    				});
    			});
    		}).on('click', '.btn-cancel-visit-coupon', function() {
    			$.cup.ajax({
    				url: '/api/v2/visitcoupons/' + $(this).data('id'),
    				method: 'delete',
    				success: function(res) {
    					loadAndRenderBook();
                    	loadAndRenderBalance();

    					_visit.settled = null;	// 재정산을 위해
    					renderVisit();

    					var visitDistrict = _districtMap[_visit.district.id];

    					if(visitDistrict.details && visitDistrict.details.kioskChargeWhenCooperatorCoupon == false)
    						return;
    					//출구에서 할인취소 시 요금정산 바로 적용
    					$.cup.ajax({
                            url: '/api/v2/machines',
                            params: {
                               type: 'PAY_STATION'
                            },
                            success: function(res) {
                               $.cup.each(res.data.machines.list, function(machine) {
                                  $.cup.ajax({
                                     url: '/api/v2/machines/' + machine.code + '/state',
                                     success: function(res) {
                                        var visit = res.data.machine.visit;
                                        if(visit && visit.id == _visit.id) {
                                        	chargeFee(_visit, machine.code, false)
                                        }
                                     }
                                  });
                               });
                            }
                         });
    				}
    			});
    		}).on('click', '.btn-cancel-all-visit-coupons', function() {
    			// 쿠폰 취소
    			$.cup.ajax({
    				url: '/api/v2/visitcoupons/visits/' + _visit.id,
    				method: 'delete',
    				success: function(res) {
    					_visit.settled = null;	// 재정산을 위해
    					renderVisit();
    					//출구에서 할인취소 시 요금정산 바로 적용
    					$.cup.ajax({
    						url: '/api/v2/machines',
    						params: {
    							type: 'PAY_STATION'
    						},
    						success: function(res) {
    							$.cup.each(res.data.machines.list, function(machine) {
    								$.cup.ajax({
    									url: '/api/v2/machines/' + machine.code + '/state',
    									success: function(res) {
    										var visit = res.data.machine.visit;

    										if(visit && visit.id == _visit.id) {
    											chargeFee(_visit, machine.code, false)
    										}
    									}
    								});
    							});
    						}
    					});
    				}
    			});

// }).on('click', '.btn-cancel-payment', function() {
// var $visit = $(this).data('record');
// // 쿠폰 취소 후 결제 취소 (무료처리 된 경우에만 사용 가능)
// $.cup.ajax({
// url: '/api/v2/visitcoupons/visits/' + $visit.id,
// method: 'delete',
// success: function(res) {
// // 결제 취소
// $.cup.ajax({
// url: '/api/v2/visits/' + $visit.id + '/unpay',
// method: 'post',
// success: function(res) {
// renderVisit();
// }
// });
// }
// });

    		}).on('click', '#btn-payment', function() {
    			/*
    			var visit = $(this).data('record');
    			if(!visit.bill.finalFee || visit.bill.finalFee == 0) {
    				$.cup.ajax({
    					url: '/api/v2/charges',
    					method: 'post',
    					params: {
    						visitId: _visit.id,
    						machineSettleCode: $.cup.member().details.machineCode,
    						settled: _visit.settled
    					},
    					success: function(res) {
    						if(res.data.visit.bill.finalFee > 0) {
    							_visit = res.data.visit;
    							renderVisitDetail();

    							$(this).click();
    						} else {
    							$.cup.toast('정산완료 되었습니다.');
    							setTimeout(function() {
    								location.href = '/';
    							}, 1000);
    						}
    					}
    				});
    				return;
    			}
    			var callbackUrl = $.cup.format('{0}/{1}/{2}/{3}/{4}', $.cup.member().details.payreturn, $.cup.member().details.van, $.cup.member().details.machineCode, $.cup.member().id, visit.id);
    			var url = $.cup.format('ecm://link?TRAN_NO={0}&TRAN_TYPE={1}&TOTAL_AMOUNT={2}&TAX={3}&&TIP={4}&INSTALLMENT={5}&RECEIPT_EMAIL={6}&RECEIPT_SMS={7}&CALL_WEB_URL={8}&ORDER_NUM={9}&CUSTOMER_CODE={10}',
    											visit.id, 'credit', visit.bill.finalFee, 0, 0, 0, '', '', callbackUrl, visit.id, visit.district.code);
    			location.href = encodeURI(url);

// $(this).prop('disabled', true);
// window.close(); // 허용되지 않음!
$('html').remove();
\*/
var visit = $(this).data('record');
$.cup.ajax({
url: '/api/v2/charges',
method: 'post',
params: {
visitId: \_visit.id,
machineSettleCode: $.cup.member().details.machineCode,  
 settled: \_visit.settled
},
success: function(res) {
if(res.data.visit.bill.finalFee > 0) {
\_visit = res.data.visit;
renderVisitDetail();

    						// PG 결제 요청
    						var callbackUrl = $.cup.format('{0}/{1}/{2}/{3}/{4}', $.cup.member().details.payreturn, $.cup.member().details.van, $.cup.member().details.machineCode, $.cup.member().id, visit.id);
    						var url = $.cup.format('ecm://link?TRAN_NO={0}&TRAN_TYPE={1}&TOTAL_AMOUNT={2}&TAX={3}&&TIP={4}&INSTALLMENT={5}&RECEIPT_EMAIL={6}&RECEIPT_SMS={7}&CALL_WEB_URL={8}&ORDER_NUM={9}&CUSTOMER_CODE={10}',
    														visit.id, 'credit', visit.bill.finalFee, 0, 0, 0, '', '', callbackUrl, visit.id, visit.district.code);
    						location.href = encodeURI(url);

// $(this).prop('disabled', true);
// window.close(); // 허용되지 않음!
$('html').remove();
} else {
$.cup.toast('정산완료 되었습니다.');
setTimeout(function() {
location.href = '/';
}, 1000);
}
}
});
return;
}).on('click', '#btn-cancel-payment', function() {
var visit = $(this).data('record');
var lastPayment = visit.payments[visit.payments.length-1];
if(!lastPayment) {
$.cup.toast('결제정보가 없습니다.', true);
return;
}
var callbackUrl = $.cup.format('{0}/{1}/{2}/{3}/{4}', $.cup.member().details.payreturn, $.cup.member().details.van, $.cup.member().details.machineCode, $.cup.member().id, visit.id);
var url = $.cup.format('ecm://link?TRAN_NO={0}&TRAN_TYPE={1}&TOTAL_AMOUNT={2}&TAX={3}&&TIP={4}&INSTALLMENT={5}&RECEIPT_EMAIL={6}&RECEIPT_SMS={7}&CALL_WEB_URL={8}&ORDER_NUM={9}&CUSTOMER_CODE={10}&APPROVAL_NUM={11}&APPROVAL_DATE={12}',
visit.id, 'credit_cancel', visit.bill.finalFee, 0, 0, 0, '', '', callbackUrl, visit.id, visit.district.code, lastPayment.authCode, lastPayment.authDate);
location.href = encodeURI(url);
// $(this).prop('disabled', true);
// window.close(); // 허용되지 않음!
$('html').remove();
}).on('click', '.btn-pop', function(){

    			var body = $(this).parent().siblings('.notice-body');

    			if(body.css('display') != 'none'){
    				body.css('display', 'none');
    			} else {
    				body.css('display', 'block');
    			}
    			$(this).toggleClass('btn-on');
    			$(this).toggleClass('btn-off');

    		}).on('click', '.btn-issue-by-balance', function() {
    			var trigger = this;
    			trigger.disabled = true;

    			var balanceId = this.value;
    			var $option = $(this).closest('tr').find('select').find('option:selected');
    			var value = $option.val();
    			var point = $option.data('point');
    			var type = $option.data('type');
    			var specialUsage = this.dataset.specialusage;
    			var label = $option.text();

    			if (!balanceId || !value) {
    				if (specialUsage != 'TIME_DEDUCTION') {
    					trigger.disabled = false;
    					return;
    				} else {
    					// 시간 차감형의 경우 필요 없는 값이라 validation을 위해 1 할당. 실제로 사용하지 않음.
    					value = 1;
    				}
    			}

    			$.cup.ajax({
    				method: 'post',
    				url: '/api/v2/visitcouponbalances/' + balanceId + '/issue',
    				params: {
    					visitId: _visit.id,
    					label: label,
    					value: value,
    					type: type,
    					point: point
    				},
    				begin: function() {
    					trigger.disabled = false;
    				},
    				success: function(res) {
    					loadAndRenderBalance();

    					_visit.settled = null;	// 재정산을 위해
    					renderVisit();


    					//--- 무인정산기에 해당 visit이 정산 중인지 확인

// $.cup.ajax({
// 	                        url: '/api/v2/machines',
// 	                        params: {
// 	                           type: 'PAY_STATION'
// 	                        },
// 	                        success: function(res) {
// 								if (record.details && record.details.payedWhenFree) {
// 									chargeFee(_visit, null, function(res) {
// 										// payedFee = 0 이면 자동으로 pay 처리 됨
//                             	  		$.cup.toast('결제처리되었습니다. 홈으로 이동합니다.');
//                             	  		setTimeout(() => {
//                             	  			location.replace('/cooperators/home');
// 										}, 2000);
//                             		});
// 								} else {
// 									$.cup.each(res.data.machines.list, function(machine) {
// 										$.cup.ajax({
// 											url: '/api/v2/machines/' + machine.code + '/state',
// 											success: function(res) {
// 												var visit = res.data.machine.visit;
// 												if(visit && visit.id == _visit.id) {
// 													// 요금 전송
// 													chargeFee(_visit, machine.code, function(res) {
// 														if(res.data.visit.leaved) {
// 															$.cup.toast('출차처리되었습니다. 홈으로 이동합니다.');
// 															setTimeout(() => {
// 																location.replace('/cooperators/home');
// 															}, 2000);
// 														}
// 													});
// 					                            }
// 											}
// 										});
// 									});
// 								}
// 	                        }
// 	                     });
					}
				});
			}).on('click', '#btn-visit-memo-register', function(ev) {
				if (!_visit) {
					return;
				}
				var dialog = $.cup.dialog({
					title: '메모',
					bodyTemplateId: 'visit-memo-dialog-template',
					data: _visit,
					tailButtons: [{
						label: '취소',
						handler: false
					}, {
						label: '저장',
						primary: true,
						handler: function() {
							var visitId = _visit.id;
							var memo = this.$dialog.find('#visit-memo').val() || null;

    						$.cup.ajax({
    							method: 'put',
    							url: '/api/v2/visits/' + _visit.id + '/memo',
    							params: {
    								memo: memo
    							},
    							success: function() {
    								_visit.memo = memo;
    								var text = memo && memo.replaceAll('\n', '<br>') || null;
    								$(ev.target).prev().html(text).toggleClass('visit-memo-exists', !!text);
    								// if(text != null) {
    								// 	$('#btn-visit-memo-register').text('메모 수정');
    								// }else {
    								// 	$('#btn-visit-memo-register').text('메모 등록');
    								// }
    								dialog.close();
    							}
    						});
    					}
    				}],
    				trigger: this,
    			});
    		});

    		function chargeFee(_visit, machineCode,synced, success) {
    			$.cup.ajax({
                    url: '/api/v2/charges',
                    method: 'post',
                    params: {
                       visitId: _visit.id,
                       // 여기서는 settled가 정해져 있는 경우 변경하면 안됨
                       settled: (_visit.settled)?
    						   $.cup.days(_visit.settled).format('YYYY-MM-DDTHH:mm:ss') : $.cup.days().format('YYYY-MM-DDTHH:mm:ss'),
    				   synced: synced ? true : !_visit.settled,
                       end: (_visit.settled)? $.cup.days(_visit.settled).format('YYYY-MM-DDTHH:mm:ss') : null,
                       machineSettleCode: machineCode ? machineCode : null
                    },
                    success: function(res) {
                    	if(success)
                    		success(res);
                    }
                 });
    		}

/_
var socket = openSocket();
function openSocket() {
return $.cup.socket('/ws/v2', {
open: function() {  
 //console.log('open', this);
},
close: function() {
//console.log('close', this);
openSocket();
},
receive: function(payload) {
console.log(payload);
if(payload.message=='payed') {
var visit = payload.data.visit;
if(visit && \_visit && visit.id == \_visit.id) {
var payment = payload.data.payment;
if(payment && payment.resCode == '0000') {
$.cup.toast('결제가 완료되었습니다.');
location.href = '/';
} else
$.cup.toast('실패하었습니다.', true);
}
}
}
});
}
_/
///////////////////////////////////////////////////////////////
var PHASE = 'PHASE2';
var $books = $('#visit-coupon-book-holder');
var $balances = $('#visit-coupon-balance-holder');

    		loadAndRenderBook();
    		loadAndRenderBalance();

    		function loadAndRenderBook() {
    			if (PHASE !== 'PHASE2') {
    				$('.phase2-section').css('display', 'none');
    				return;
    			}
    			$.cup.ajax({
    				url: '/api/v2/members/27/availablebooks',
    				success: function(res) {
    					availableBooks = res.data.availableBooks || [];
    					if (!availableBooks.length) {
    						$books.closest('.app-section-body').hide();
    						return;
    					} else {
    						$books.closest('.app-section-body').show();
    					}
    					$books.table({
    						columns: [{
    							label: '쿠폰 종류',
    							render: function(book) {
    								return book.name;
    							}
    						}, {
    							label: '유/무료',
    							render: function(book) {
    								if (book && book.notFree) {
    									return '유료';
    								} else {
    									return $.cup.format('<b style="color: {0};">{1}</b>', '#2196f3', '무료');
    								}
    							}
    						}, {
    							label: '할당 수량',
    							render: function(book) {
    								return book.totalNumberOfIssuance ? book.totalNumberOfIssuance : '무제한';
    							}
    						}, {
    							label: '잔여 수량',
    							render: function(book) {
    								return book.totalNumberOfIssuance ? book.totalNumberOfIssuance - book.issuedCount : '무제한';
    							}
    						}],
    						records: availableBooks
    					});
    				}
    			});
    		}

    		function loadAndRenderBalance() {
    			if (PHASE !== 'PHASE2') {
    				return;
    			}
    			$.cup.ajax({
    				url: '/api/v2/visitcouponbalances',
    				params: $.cup.pageless({
    					sort: 'template.name',
    					memberId: '27',
    					unclosed: true
    				}),
    				success: function(res) {
    					if (!res.data.visitCouponBalances.totalItems) {
    						$balances.closest('.app-section-body').hide();
    						return;
    					} else {
    						$balances.closest('.app-section-body').show();
    					}
    					$balances.table({
    						columns: [{
    							label: '쿠폰 종류',
    							render: 'template.name'
    						}, {
    							label: '유/무료',
    							render: function(balance) {
    								if (balance.template && balance.template.notFree) {
    									return '유료';
    								} else {
    									return $.cup.format('<b style="color: {0};">{1}</b>', '#2196f3', '무료');
    								}
    							}
    						}, {
    							label: '잔여 포인트',
    							render: 'pointsBalance'
    						}],
    						records: filterBalances(res.data.visitCouponBalances.list)
    					});
    				}
    			});
    		}

    		function filterBalances(originals) {
    			const data = {};
    			const order = [];

    			for (let i = 0, b; b = originals[i++];) {
    				const prev = data[b.template.id];

    				if (!prev || prev.created < b.created) {
    					order.push(b.template.id);
    					data[b.template.id] = b;
    				}
    			}
    			const balances = [];

    			for (let j = 0, k; k = order[j++];) {
    				balances.push(data[k]);
    			}
    			return balances;
    		}

    		function getType(balance) {
    			switch (balance.type) {
    			case 'RESET':
    				return '충전';
    			case 'DEPOSIT':
    				return '적립';
    			case 'ISSUE':
    				return '발급';
    			case 'CANCEL':
    				return '취소';
    			default:
    				return '-';
    			}
    		}
    		// 계산기 시작
    		virtualCalculator();

    	})(jQuery);

    	function seasonTicketDurationOn() {
    		$('#duration-detail').show();
    	}
    	function seasonTicketDurationOut() {
    		$('#duration-detail').hide();
    	}

    </script>
    <script id="coupon-control-template" type="text/x-handlebars-template">
    	<table class="gbox-table">
    		<tbody class="gbox-body" data-record="{{json visit}}">
    			<tr class="gbox-body-row">
    				<td class="gbox-head-cell">차량번호</td>
    				<td class="gbox-body-cell">{{visit.lpn}}
    					{{#if (or visit.kakaoTid (and visit.details visit.details.kakaoT_kakao_id))}}
    						&nbsp;
    						{{#if visit.details.kakaoT_auto_exit}}
    							<b style="color: #000; background-color: #ffcd00;">T주차</b>
    						{{else}}
    							<b style="color: #000; background-color: #ffcd00;">T주차(감면)</b>
    						{{/if}}
    					{{/if}}
    					<button id="btn-visit-memo-register" type="button" class="btn" value="{{visit.id}}">메모</button>
    				</td>
    			</tr>
    			{{#if visit.seasonTicket}}
    			<tr class="gbox-body-row">
    				<td class="gbox-head-cell">

<b style="color: #ff5c01;">정기권</b>
{{#if (empty visit.settled)}}
{{#if (gt now visit.seasonTicket.duration.end)}}<b style="color:#f00; font-size:14px;">(만료)</b>{{else}}(유효){{/if}}
{{else}}
{{#if (gt visit.settled visit.seasonTicket.duration.end)}}<b style="color:#f00; font-size:14px;">(만료)</b>{{else}}(유효){{/if}}
{{/if}}
</td>
<td class="gbox-body-cell">

    					{{#if (contains visit.seasonTicket.duration.start '00:00:00')}}
    						{{datetime visit.seasonTicket.duration.start 'YYYY-MM-DD'}} ~
    					{{else}}
    						{{datetime visit.seasonTicket.duration.start 'YYYY-MM-DD HH:mm:ss'}} ~
    					{{/if}}
    					{{#if (contains visit.seasonTicket.duration.end '23:59:59')}}
    						{{datetime visit.seasonTicket.duration.end 'YYYY-MM-DD'}}
    					{{else if (contains visit.seasonTicket.duration.end '00:00:00')}}
    						{{datetime (prevDate visit.seasonTicket.duration.end) 'YYYY-MM-DD'}}
    					{{else}}
    						{{datetime visit.seasonTicket.duration.end 'YYYY-MM-DD HH:mm:ss'}}
    					{{/if}}

    					{{#if visit.seasonTicket.seasonTicketTemplate}}
    						<br>({{visit.seasonTicket.seasonTicketTemplate.name}})
    					{{else if visit.seasonTicket.bandStart}}
    						<br>({{time visit.seasonTicket.bandStart false}} ~ )
    					{{/if}}
    					{{#if visit.seasonTicket.seasonTicketTemplate.timetable}}
    					<img id="season-duration" src="../../resources/img/icon-menu-search.png" style="cursor:pointer;width:18px;height:18px;position:absolute;margin-top:3px;" onmouseenter="seasonTicketDurationOn();" onmouseleave="seasonTicketDurationOut();";/>
    					<div id="duration-detail" style="position:absolute;border:1px solid black;padding:2px;margin-left:5%;z-index:1;background:white;display:none;">
    						정기권 유효시간<br>{{#each visit.seasonTicket.seasonTicketTemplate.timetable}}{{#if (eq this.dayOfWeek 'MONDAY')}}(월){{else if (eq this.dayOfWeek 'TUESDAY')}}(화){{else if (eq this.dayOfWeek 'WEDNESDAY')}}(수){{else if (eq this.dayOfWeek 'THURSDAY')}}(목){{else if (eq this.dayOfWeek 'FRIDAY')}}(금){{else if (eq this.dayOfWeek 'SATURDAY')}}(토){{else if (eq this.dayOfWeek 'SUNDAY')}}(일){{/if}} {{this.start}}~{{this.end}}<br>{{/each}}
    					</div>
    					{{/if}}
    				</td>
    			</tr>
    			{{/if}}
    			<tr class="gbox-body-row">
    				<td class="gbox-head-cell">입차 시각</td>
    				<td class="gbox-body-cell">{{datetime visit.entered 'YYYY-MM-DD HH:mm:ss'}}</td>
    			</tr>

<tr class="gbox-body-row">
					<td class="gbox-head-cell">주차 시간</td>
					<td class="gbox-body-cell">{{duration}} <span style="color:darkred">({{currency visit.bill.finalFee}}원)</span></td>
				</tr>
<tr class="gbox-body-row">
					<td class="gbox-head-cell">할인 내역</td>
					<td class="gbox-body-cell">
						{{#each visitCoupons}}
							<div class="qbox-filter-field">
								{{visitCouponTemplate.name}}
								{{#if label}} / {{label}}{{/if}}
								/ {{creator.name}}
								{{#if (eq creator.id ../member.id)}}
								&nbsp;<button type="button" class="btn btn-inline btn-cancel-visit-coupon" data-id="{{id}}">X</button>
								{{/if}}
							</div>
						{{/each}}
</td>
				</tr>
				{{#if (empty visit.leaved)}}
				{{#each visitCouponBooks}}
						{{#if (ne disabled true)}}
							<tr class="gbox-body-row">
								<td class="gbox-body-cell" colspan="2">
									<button class="btn btn-primary btn-visit-coupon btn-visit-coupon-prevent"
											style="width: 100%; height: 40px; line-height: 40px; font-size: 16px;" data-record="{{json this}}"
											{{disabled isButtonDisable}}
									>{{name}}
										
										{{#if (exists totalNumberOfIssuance)}}
											[남은수량:{{substract totalNumberOfIssuance issuedCount}}]
										{{else}}
											[무제한]
										{{/if}}
									</button>
								</td>
							</tr>
						{{/if}}
				{{/each}}
				{{#if (notEmpty visitCouponBalances)}}
					<tr class="gbox-body-row">
						<td class="gbox-body-cell" colspan="2">
							<table>
								{{#each visitCouponBalances}}
									<tr>
										<th>
											<p>{{name}}</p>
										</th>
										{{#if (eq specialUsage 'TIME_DEDUCTION')}}
										<td>
											<p>잔여 포인트: {{pointsBalance}}</p>
										</td>
										{{else}}
										<td>
											<select class="sbox" {{disabled disabled}}>
												{{#each buttons}}
													<option value="{{value}}" data-point="{{point}}" data-type="{{type}}" {{disabled disabled}}>{{label}}</option>
												{{/each}}
											</select>
										</td>
										{{/if}}
										<td>
											<button class="btn btn-primary btn-issue-by-balance" style="display:block;width:100%"
													data-specialUsage="{{specialUsage}}" value="{{id}}" {{disabled disabled}} >발급</button>
										</td>
									</tr>
								{{/each}}
							</table>
						</td>
					</tr>
				{{/if}}
{{/if}}

    			{{#if (and member.details member.details.van)}}
    				{{#if (gt visit.payedFeeCredit 0)}}
    				<tr class="gbox-body-row">
    					<td class="gbox-body-cell car-image-holder" colspan="2">
    						<button id="btn-cancel-payment" class="btn btn-primary btn-red" style="width: 100%; height: 40px; line-height: 40px; font-size: 16px; text-align: center; color: #ff5c01; border-color: #ff5c01; background-color: #fff;" data-record="{{json visit}}">결제 취소</button>
    					</td>
    				</tr>
    				{{else}}
    				<tr class="gbox-body-row">
    					<td class="gbox-body-cell car-image-holder" colspan="2">
    						<button id="btn-payment" class="btn btn-primary btn-red" style="width: 100%; height: 40px; line-height: 40px; font-size: 16px; text-align: center; color: #fff; border-color: #ff5c01; background-color: #ff5c01;" data-record="{{json visit}}">결제</button>
    					</td>
    				</tr>
    				{{/if}}
    			{{/if}}
    			<tr class="gbox-body-row">
    				<td class="gbox-body-cell car-image-holder" colspan="2">
    					<img src="/car_images/{{visit.images.IN}}" style="width: 100%;">
    					<span class="car-image-lpn">{{visit.lpn}}</span>
    				</td>
    			</tr>
    		</tbody>
    	</table>
    </script>
    <script id="notice-body-template" type="text/x-handlebars-template">
    	{{#if (not empty notices)}}
    		{{#each notices}}
    			<div class="notice-body">
    			</div>
    		{{/each}}
    	{{/if}}
    </script>

</body>
