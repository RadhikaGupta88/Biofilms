function[] = Remove_Biofilm_Interior_Noise(daynumber,lighttype,bridging,smoothingkernal_sd,bwthreshold)

% DAYNUMBER indicates the day of the experiment
% DAYNUMBER = 1 -> 200920

% LIGHTTYPE indicates whether the video we are considering brightfield or
% bio-light
% LIGHTTYPE = 0 -> Brightfield
% LIGHTTYPE = 1 -> Bio-light

% We take a video of the evolution of a biofilm which has been preprocessed
% in ImageJ and clean it up using the MATLAB image processing toolbox 
%(imfill, bwareaflt, bwmorph etc)

% In some videos, due to variable lighting the boundary of the biofilm has
% gaps in it. Thus if BRIDGING is 1 we use the bridge element in bwmorph to
% fill these gaps

% In some videos, the edge of a biofilm is not well defined due to long
% polymer strands. Thus if SMOOTHINGKERNAL_SD is greater than 1 we utilise
% IMGAUSSFILT which utilises a 2D Gaussian smooting kernal with standard
% deviation SMOOTHKERNAL_SD together with IMBINARIZE using a threshold of
% BWTHRESHOLD to blur out the strands which are typically very thin and 
% thus a bit of white surrounded by black and keep the main biofilm which 
% is white surrounded by white.

if daynumber == 1
    daydate = '200920';
end

if lighttype == 0
    lightname = 'normallight';
elseif lighttype == 1
    lightname = 'biolight';
end

% Read initial processed in imagej video
readfilelocation = strcat(daydate,'_',lightname,'_bw_imagej.avi');

if smoothingkernal_sd > 1
    writefilelocationbw = strcat(daydate,'_',lightname,'_bw_smoothingkernal_sd',num2str(smoothingkernal_sd),'.avi');            
else
    writefilelocationbw = strcat(daydate,'_',lightname,'_bw.avi');
end
disp(readfilelocation);
disp(writefilelocationbw);
    
vid = VideoReader(readfilelocation);
framerate = vid.FrameRate;
numframes = vid.NumberOfFrames;
width = vid.Width;
height = vid.Height;
fprintf('Width is %4.2f, Height is %4.2f, Frame rate is %4.2f and the number of frames is %4.2f\n',width,height,framerate,numframes);
vid = VideoReader(readfilelocation);
writerObjbw = VideoWriter(writefilelocationbw);
writerObjbw.FrameRate = 50;
open(writerObjbw);

for a = 1 : numframes
    % Read a frame of the video
    f = readFrame(vid);
    % WLOG we take the red channel
    g0 = f(:,:,1);
    % If we are dealing with a biofilm with strands, we use imgaussfult to
    % remove them
    if smoothingkernal_sd > 1
        g0 = imgaussfilt(g0,smoothingkernal_sd);
    end
    % Then we turn it to a bw image using the threshold bwthreshold 
    % (typically we set the threshold to 110)
    g1 = imbinarize(g0,bwthreshold/255);  
    % Fill in gaps in the edge if necessary using bwmorph
    if bridging == 1
        g2 = bwmorph(g1,'bridge');
    else
        g2 = g1;
    end
    % The biofilm can run off the top and the bottom edge so we add
    % temporary strips of white to put both bits of the boundary together
    g3 = ones([height+2,width]);
    g3(2:height+1,1:width) = g2;    
    % Now that we have a closed boundary we can fill in the holes with
    % white pixels
    g3 = imfill(g3,'holes');
    g3 = g3(2:height-1,1:width);
    g3 = logical(g3);
    % We select the largest white region which is our biofilm
    g4 = bwareafilt(g3,1);
    g5 = 255 * uint8(g4);
    % We save the resulting image
    writeVideo(writerObjbw,g5);
    if a == 1
        % Just as a sanity check lets look at frame 100
        figure;
        imshow(g1);
        figure;
        imshow(g2);
        figure;
        imshow(g3);
        figure;
        imshow(g4);
    end
end
close(writerObjbw);