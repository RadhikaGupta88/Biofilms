function[] = Experimental_Radius_Locator(daynumber,lighttype,include_smoothing)

% Locates the position of the biofilm interface and calculates the centre
% of the biofilm / the radius of the biofilm by fitting a circle. We then
% superimpose this onto the orginal video to get a pretty video

% DAYNUMBER indicates the day of the experiment
% DAYNUMBER = 1 -> 200920

% LIGHTTYPE indicates whether the video we are considering brightfield or
% bio-light
% LIGHTTYPE = 0 -> Brightfield
% LIGHTTYPE = 1 -> Bio-light

% If INCLUDE_SMOOTHING  is 1, we have in the preprocessing already used
% guassian smoothing

full_xlocations = [];
full_ylocations = [];
full_theta_values = linspace(0,2*pi,1000);
current_folder = pwd;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Here we open two files for reading (the orginal video and the processed
% video that just has the biofilm interface and one file for writing to
% save the final pretty video
if include_smoothing == 1
    smoothing_part = '_smoothingkernal_sd8';
else
    smoothing_part = '';
end

% NOTE frame_interval is the time in minutes between frames while
% lengthscale is the length in mm of one pixel in a video
if daynumber == 1
    daydate = '200920';
    if lighttype == 0
        lightname = 'normallight';
        frame_interval = 1;
        lengthscale = 1;
    elseif lighttype == 1
        lightname = 'biolight';
        frame_interval = 1;
        lengthscale = 1;
    end
end

readedgefilelocation = strcat(daydate,'_',lightname,'_bw_edge',smoothing_part,'.avi');
readfullvideofilelocation = strcat(daydate,'_',lightname,'_orginal.avi');
writefilelocation = strcat(daydate,'_',lightname,'_pretty_biofilm',smoothing_part,'.avi');   
disp(readedgefilelocation);
disp(readfullvideofilelocation);
disp(writefilelocation);

writerObj = VideoWriter(writefilelocation);
writerObj.FrameRate = 50;
open(writerObj);

edge_vid = VideoReader(readedgefilelocation);
edgeframerate = edge_vid.FrameRate;
edgenumframes = edge_vid.NumberOfFrames;
edgewidth = edge_vid.Width;
edgeheight = edge_vid.Height;
fprintf('Width is %4.2f, Height is %4.2f, Frame rate is %4.2f and the number of frames is %4.2f\n',edgewidth,edgeheight,edgeframerate,edgenumframes);
edge_vid = VideoReader(readedgefilelocation);

full_vid = VideoReader(readfullvideofilelocation);
fullvideoframerate = full_vid.FrameRate;
fullvideonumframes = full_vid.NumberOfFrames;
fullvideowidth = full_vid.Width;
fullvideoheight = full_vid.Height;
fprintf('Width is %4.2f, Height is %4.2f, Frame rate is %4.2f and the number of frames is %4.2f\n',fullvideowidth,fullvideoheight,fullvideoframerate,fullvideonumframes);
full_vid = VideoReader(readfullvideofilelocation);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Contains the radius of the biofilm
Rvalues = zeros([1,edgenumframes]);
% Contains the x coordinate of the biofilm centre
Rcentre_x = zeros([1,edgenumframes]);
% Contains the y coordinate of the biofilm centre
Rcentre_y = zeros([1,edgenumframes]);
% Contains the time values for each frame in hours
tvalues = (((1:edgenumframes) - 1) * frame_interval)/60;

figure;
for a = 1 : edgenumframes
    f = readFrame(edge_vid);
    g0 = f;    
    full_xlocations = [];
    full_ylocations = [];
    % Locates the (x,y) position of each point on the interface. Since for
    % this at the moment we dont care about finding the points in order we
    % just sweep through the array column by column (Note if you decide you
    % want to do this let me know since I also have code to do this, it is
    % just more complicated
    for b = 1 : edgewidth
        for c = 1 : edgeheight
            if g0(c,b) == 255
                full_xlocations = [full_xlocations,b];
                full_ylocations = [full_ylocations,c];
            end
        end
    end
    % Cheap and Cheerful fitting a circle using the function circfit. There
    % are more robust ways to do this using a least squares fit but for
    % this the interface is simple enough that I dont think it is necessary
    % (Of course if you want to do this let me know and I can send you code
    % to do this)
    [xc,yc,R,~] = circfit(full_xlocations,full_ylocations);
    [theta_values,r_values] = cart2pol(full_xlocations-xc,full_ylocations-yc); 
    Rvalues(a) = R;
    Rcentre_x(a) = xc;
    Rcentre_y(a) = yc;
    % full circle xvalues and yvalues are just points on the fitted circle
    % where we start with all possible theta values and then exclude any
    % point that will be off the initial image
    full_circle_xvalues = xc + R * cos(full_theta_values); 
    full_circle_yvalues = yc + R * sin(full_theta_values);
    full_circle_xvalues(full_circle_yvalues < 1) = [];
    full_circle_yvalues(full_circle_yvalues < 1) = [];
    full_circle_yvalues(full_circle_xvalues < 1) = [];
    full_circle_xvalues(full_circle_xvalues < 1) = []; 
    full_circle_xvalues(full_circle_yvalues > edgeheight) = [];
    full_circle_yvalues(full_circle_yvalues > edgeheight) = [];
    full_circle_xvalues(full_circle_xvalues > edgewidth) = [];
    full_circle_yvalues(full_circle_xvalues > edgewidth) = [];   
    % Now we generate a pretty video by superimposing the located interface
    % and the fitted circle onto the orginal video
    gfull = readFrame(full_vid);
    imshow(gfull);
    hold on;
    plot(full_xlocations,full_ylocations,'.b')
    plot(full_circle_xvalues,full_circle_yvalues,'-r')
    hold off;
    my_figure = getframe(gcf);
    writeVideo(writerObj, my_figure);
    % Finally we save our data namely the located interface blue points and
    % the fitted circle red points
    red_table = table(full_circle_xvalues.', full_circle_yvalues.', 'VariableNames', {'FittedRedCircleXpoints', 'FittedRedCircleYpoints'});
    writetable(red_table, strcat(current_folder,'\Data_Storage\',daydate,'\red_fitted_points\',daydate,'_',lightname,'_red_fitted_points_numframe=',num2str(a),'.txt'));
    blue_table = table(full_xlocations.', full_ylocations.',r_values.',theta_values.', 'VariableNames', {'BlueInterfaceXpoints', 'BlueInterfaceYpoints','BlueInterfaceRValues','BlueInterfaceThetaValues'});
    writetable(blue_table, strcat(current_folder,'\Data_Storage\',daydate,'\blue_interface_points\',daydate,'_',lightname,'_blue_interface_points_numframe=',num2str(a),'.txt'));
end
close(writerObj);

% We plot how the radius of the biofilm varies with time
figure;
normalisedRvalues = Rvalues/Rvalues(1);
plot(tvalues,normalisedRvalues,'.');
% For later use we generate two tables, ie one with just the normalised
% radius as a function of time and one with the radius and location of the 
% centre of the fitted circle
T1 = table(tvalues.', normalisedRvalues.', 'VariableNames', {'Time', 'ExperimentalDataPoints'});
writetable(T1, strcat(current_folder,'\Data_Storage\',daydate,'\',daydate,'_',lightname,smoothing_part,'.txt'));
circlecentre_position_table = table(tvalues.',Rvalues.',Rcentre_x.',Rcentre_y.','VariableNames', {'Time', 'FittedRadius','FittedCirclex','FittedCircley'});
writetable(circlecentre_position_table, strcat(current_folder,'\Data_Storage\',daydate,'\',daydate,'_',lightname,smoothing_part,'_fitted_circle_position_data.txt')); 
    
